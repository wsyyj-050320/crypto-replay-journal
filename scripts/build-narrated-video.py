from __future__ import annotations

from pathlib import Path
import asyncio
import subprocess

import imageio_ffmpeg


ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "video"

SCRIPT_TEXT = (
    "Meet Crypto Replay Journal. A sharper way to review crypto trades. "
    "Scan unusual moves, track paper equity, and keep drawdown in view. "
    "Filter risk context without turning alerts into advice. "
    "Replay decisions candle by candle, compare exits, and write the lesson down. "
    "Then finish the day with a clean research report. "
    "No directional calls. No financial advice."
)

SRT = """1
00:00:00,000 --> 00:00:05,000
Meet Crypto Replay Journal. A sharper way to review crypto trades.

2
00:00:05,000 --> 00:00:10,000
Scan unusual moves, track paper equity, and keep drawdown in view.

3
00:00:10,000 --> 00:00:15,000
Filter risk context without turning alerts into advice.

4
00:00:15,000 --> 00:00:20,000
Replay decisions candle by candle, compare exits, and write the lesson down.

5
00:00:20,000 --> 00:00:25,000
Then finish the day with a clean research report.

6
00:00:25,000 --> 00:00:30,000
No directional calls. No financial advice.
"""


async def synthesize_edge_mp3(text_path: Path, mp3_path: Path) -> None:
    import edge_tts

    text = text_path.read_text(encoding="utf-8")
    communicate = edge_tts.Communicate(
        text,
        voice="en-US-BrianNeural",
        rate="+8%",
        pitch="+5Hz",
        volume="+0%",
    )
    await communicate.save(str(mp3_path))


def synthesize_wav(text_path: Path, wav_path: Path) -> None:
    ps_script = f"""
$text = Get-Content -LiteralPath "{text_path}" -Raw
$voice = New-Object -ComObject SAPI.SpVoice
$voice.Rate = 0
$voice.Volume = 92
$stream = New-Object -ComObject SAPI.SpFileStream
$stream.Open("{wav_path}", 3, $false)
$voice.AudioOutputStream = $stream
$voice.Speak($text) | Out-Null
$stream.Close()
"""
    subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
        check=True,
    )


def mux_audio(video_path: Path, audio_path: Path, out_path: Path) -> None:
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run(
        [
            ffmpeg,
            "-y",
            "-i",
            str(video_path),
            "-i",
            str(audio_path),
            "-filter_complex",
            "[1:a]apad=pad_dur=12[a]",
            "-map",
            "0:v:0",
            "-map",
            "[a]",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-shortest",
            str(out_path),
        ],
        check=True,
    )


def main() -> None:
    VIDEO.mkdir(exist_ok=True)
    text_path = VIDEO / "narration.txt"
    srt_path = VIDEO / "narration.srt"
    wav_path = VIDEO / "narration.wav"
    mp3_path = VIDEO / "narration-energetic-male.mp3"
    video_path = VIDEO / "crypto-replay-journal-promo.mp4"
    out_path = VIDEO / "crypto-replay-journal-promo-narrated.mp4"

    text_path.write_text(SCRIPT_TEXT, encoding="utf-8")
    srt_path.write_text(SRT, encoding="utf-8")
    try:
        asyncio.run(synthesize_edge_mp3(text_path, mp3_path))
        audio_path = mp3_path
    except Exception as exc:
        print(f"Edge TTS failed, falling back to local SAPI voice: {exc}")
        synthesize_wav(text_path, wav_path)
        audio_path = wav_path
    mux_audio(video_path, audio_path, out_path)
    print("Built narrated video, narration text, WAV, and SRT.")


if __name__ == "__main__":
    main()
