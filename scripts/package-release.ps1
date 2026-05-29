param(
    [string]$Version = "0.1.0"
)

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$releaseDir = Join-Path $root "release"
$zipName = "crypto-replay-journal-v$Version.zip"
$zipPath = Join-Path $releaseDir $zipName
$stage = Join-Path $releaseDir "crypto-replay-journal"

if (Test-Path -LiteralPath $stage) {
    Remove-Item -LiteralPath $stage -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $stage | Out-Null

$excludeDirs = @(
    ".git",
    "node_modules",
    "release",
    "__pycache__"
)

$excludeFiles = @(
    "*.zip",
    "*.pyc",
    ".DS_Store",
    "Thumbs.db"
)

Get-ChildItem -LiteralPath $root -Force | ForEach-Object {
    $name = $_.Name
    if ($excludeDirs -contains $name) {
        return
    }

    $excludedFile = $false
    foreach ($pattern in $excludeFiles) {
        if ($name -like $pattern) {
            $excludedFile = $true
            break
        }
    }
    if ($excludedFile) {
        return
    }

    Copy-Item -LiteralPath $_.FullName -Destination $stage -Recurse -Force
}

Get-ChildItem -LiteralPath $stage -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
Get-ChildItem -LiteralPath $stage -Recurse -File -Filter "*.pyc" | Remove-Item -Force

if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}

Compress-Archive -LiteralPath $stage -DestinationPath $zipPath -CompressionLevel Optimal
Write-Output $zipPath
