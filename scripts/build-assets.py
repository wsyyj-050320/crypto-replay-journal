from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math
import textwrap

import imageio.v2 as imageio
from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
SCREENSHOTS = ASSETS / "screenshots"
VIDEO = ROOT / "video"

INK = (24, 35, 38)
MUTED = (94, 109, 113)
PAPER = (247, 248, 246)
PANEL = (255, 255, 255)
LINE = (220, 228, 226)
ACCENT = (23, 125, 114)
AMBER = (159, 116, 25)
RED = (174, 68, 59)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def fit_image(path: Path, size: tuple[int, int], crop: bool = True) -> Image.Image:
    image = Image.open(path).convert("RGB")
    if crop:
        return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.22))
    image.thumbnail(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, PAPER)
    canvas.paste(image, ((size[0] - image.width) // 2, (size[1] - image.height) // 2))
    return canvas


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font_obj: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
    width: int,
    line_gap: int = 8,
) -> int:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font_obj)[2] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += font_obj.size + line_gap
    return y


def draw_button(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, dark: bool = True) -> None:
    x, y = xy
    pad_x, pad_y = 22, 12
    label_font = font(24, True)
    box = draw.textbbox((0, 0), text, font=label_font)
    width = box[2] - box[0] + pad_x * 2
    height = box[3] - box[1] + pad_y * 2
    fill = INK if dark else PAPER
    outline = INK if dark else LINE
    text_fill = (255, 255, 255) if dark else INK
    draw.rounded_rectangle((x, y, x + width, y + height), radius=0, fill=fill, outline=outline)
    draw.text((x + pad_x, y + pad_y - 2), text, font=label_font, fill=text_fill)


def draw_browser_frame(canvas: Image.Image, image_path: Path, box: tuple[int, int, int, int]) -> None:
    draw = ImageDraw.Draw(canvas)
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=PANEL, outline=LINE)
    draw.rectangle((x1, y1, x2, y1 + 42), fill=(237, 242, 240), outline=LINE)
    for index, color in enumerate([(166, 179, 177), (188, 198, 196), (132, 150, 146)]):
        cx = x1 + 22 + index * 18
        draw.ellipse((cx, y1 + 15, cx + 10, y1 + 25), fill=color)
    shot = fit_image(image_path, (x2 - x1, y2 - y1 - 42), crop=True)
    canvas.paste(shot, (x1, y1 + 42))


def make_social_og() -> None:
    canvas = Image.new("RGB", (1200, 630), PAPER)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 1200, 630), fill=PAPER)
    draw.rectangle((0, 0, 1200, 72), fill=PANEL)
    draw.rectangle((48, 22, 88, 62), fill=INK)
    draw.text((59, 31), "CR", font=font(16, True), fill=(255, 255, 255))
    draw.text((104, 27), "Crypto Replay Journal", font=font(27, True), fill=INK)

    draw.text((70, 150), "OPEN-SOURCE RISK REVIEW", font=font(18, True), fill=ACCENT)
    y = draw_wrapped(
        draw,
        (70, 188),
        "Paper trading, replay, and risk journaling for crypto decisions.",
        font(58, True),
        INK,
        500,
        10,
    )
    y += 12
    draw_wrapped(
        draw,
        (70, y),
        "No directional calls. No performance promises. Just better review.",
        font(26),
        MUTED,
        470,
        8,
    )
    draw_button(draw, (70, 514), "Open product demo", dark=True)
    draw_browser_frame(canvas, SCREENSHOTS / "demo.png", (620, 126, 1140, 536))
    canvas.save(ASSETS / "social-og.png", quality=95)


def make_thumbnail() -> None:
    canvas = Image.new("RGB", (1280, 720), (236, 242, 240))
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 1280, 720), fill=(236, 242, 240))
    draw_browser_frame(canvas, SCREENSHOTS / "demo.png", (520, 86, 1210, 632))
    draw.rectangle((0, 0, 520, 720), fill=(16, 32, 34))
    draw.text((58, 72), "CRYPTO REPLAY JOURNAL", font=font(22, True), fill=(101, 205, 191))
    draw_wrapped(draw, (58, 128), "Review trades. Replay risk.", font(66, True), (255, 255, 255), 390, 10)
    draw_wrapped(
        draw,
        (58, 366),
        "A paper trading and risk journal for crypto traders.",
        font(28),
        (199, 215, 211),
        390,
        8,
    )
    draw.text((58, 610), "No directional calls. Not financial advice.", font=font(20, True), fill=(199, 215, 211))
    canvas.save(ASSETS / "video-thumbnail-clean.png", quality=95)


def make_gallery_card(index: int, title: str, subtitle: str, screenshot: Path, accent: tuple[int, int, int]) -> None:
    gallery = ASSETS / "gallery"
    gallery.mkdir(exist_ok=True)
    canvas = Image.new("RGB", (1600, 1000), PAPER)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, 1600, 1000), fill=PAPER)
    draw.rectangle((0, 0, 1600, 92), fill=PANEL)
    draw.rectangle((64, 26, 110, 72), fill=INK)
    draw.text((78, 38), "CR", font=font(18, True), fill=(255, 255, 255))
    draw.text((132, 32), "Crypto Replay Journal", font=font(31, True), fill=INK)
    draw.text((78, 174), f"0{index}", font=font(22, True), fill=accent)
    y = draw_wrapped(draw, (78, 214), title, font(72, True), INK, 560, 8)
    draw_wrapped(draw, (78, y + 22), subtitle, font(31), MUTED, 540, 8)
    draw_browser_frame(canvas, screenshot, (760, 170, 1510, 794))
    draw.text((78, 886), "No directional calls. Not financial advice.", font=font(24, True), fill=MUTED)
    canvas.save(gallery / f"product-hunt-{index:02d}.png", quality=95)


def make_product_hunt_gallery() -> None:
    cards = [
        (
            "Paper trading, replay, and risk review.",
            "A concrete workspace for reviewing crypto decisions without turning alerts into advice.",
            SCREENSHOTS / "demo.png",
            ACCENT,
        ),
        (
            "Start with risk context.",
            "Track anomalies, equity, drawdown, daily loss, and recent simulated trades in one view.",
            SCREENSHOTS / "demo.png",
            AMBER,
        ),
        (
            "End with a daily review report.",
            "Summarize market context, paper performance, largest loss, and tomorrow's watchlist.",
            SCREENSHOTS / "report.png",
            RED,
        ),
        (
            "Built for open-source trust.",
            "Sample data, visible assumptions, and research-only language from the first screen.",
            SCREENSHOTS / "home.png",
            ACCENT,
        ),
    ]
    for index, card in enumerate(cards, start=1):
        make_gallery_card(index, *card)


@dataclass
class Scene:
    title: str
    subtitle: str
    image: Path
    accent: tuple[int, int, int] = ACCENT


def draw_scene(scene: Scene, progress: float, size: tuple[int, int] = (1280, 720)) -> Image.Image:
    width, height = size
    eased = 1 - math.pow(1 - progress, 3)
    canvas = Image.new("RGB", size, PAPER)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle((0, 0, width, height), fill=PAPER)
    draw.rectangle((0, 0, width, 68), fill=PANEL)
    draw.rectangle((42, 18, 78, 54), fill=INK)
    draw.text((51, 26), "CR", font=font(15, True), fill=(255, 255, 255))
    draw.text((96, 24), "Crypto Replay Journal", font=font(25, True), fill=INK)

    image_x = int(512 + (1 - eased) * 38)
    draw_browser_frame(canvas, scene.image, (image_x, 118, 1224, 618))

    text_y = int(145 + (1 - eased) * 18)
    draw.text((58, text_y), "PRODUCT DEMO", font=font(18, True), fill=scene.accent)
    next_y = draw_wrapped(draw, (58, text_y + 42), scene.title, font(58, True), INK, 420, 9)
    draw_wrapped(draw, (58, next_y + 22), scene.subtitle, font(25), MUTED, 410, 8)
    draw.rectangle((58, 646, 1222, 652), fill=(218, 226, 224))
    draw.rectangle((58, 646, int(58 + 1164 * progress), 652), fill=scene.accent)
    return canvas


def make_video() -> None:
    VIDEO.mkdir(exist_ok=True)
    scenes = [
        Scene(
            "Review crypto trades without turning alerts into advice.",
            "Paper trading, strategy replay, and risk journaling in one local workspace.",
            SCREENSHOTS / "home.png",
        ),
        Scene(
            "Start with risk context.",
            "Track anomalies, drawdown, worst daily loss, and recent paper trades.",
            SCREENSHOTS / "demo.png",
        ),
        Scene(
            "Scan unusual moves, not instructions.",
            "Market anomaly, volatility, and momentum context stay separate from decisions.",
            SCREENSHOTS / "demo.png",
            AMBER,
        ),
        Scene(
            "Replay the decision candle by candle.",
            "Compare fixed targets, trailing exits, and no-stop risk on the same move.",
            SCREENSHOTS / "demo.png",
        ),
        Scene(
            "End the day with a review artifact.",
            "Generate a daily market and paper trade review with assumptions visible.",
            SCREENSHOTS / "report.png",
            RED,
        ),
        Scene(
            "No directional calls. No performance promises.",
            "For research and educational use only. Not financial advice.",
            SCREENSHOTS / "report.png",
        ),
    ]
    fps = 24
    seconds_per_scene = 5
    frames = []
    for scene in scenes:
        for frame_index in range(fps * seconds_per_scene):
            progress = frame_index / (fps * seconds_per_scene - 1)
            frames.append(draw_scene(scene, progress))
    out = VIDEO / "crypto-replay-journal-promo.mp4"
    imageio.mimsave(out, frames, fps=fps, quality=8, macro_block_size=16)


def main() -> None:
    make_social_og()
    make_thumbnail()
    make_product_hunt_gallery()
    make_video()
    print("Built social images and promo video.")


if __name__ == "__main__":
    main()
