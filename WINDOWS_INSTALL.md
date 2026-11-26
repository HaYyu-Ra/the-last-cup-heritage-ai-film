# Windows Installation

## Prerequisites
1. Install Python 3.11 or newer.
2. Install FFmpeg and ensure `ffmpeg` is available on PATH.
3. Download or clone this repository.

## Create the environment
Open PowerShell in the repository directory:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If script execution is blocked, run `Set-ExecutionPolicy -Scope Process Bypass` in that PowerShell window.

## Validate and render

```powershell
ffmpeg -version
python -m pipeline.validate
python -m pipeline.run
```

Final MP4 files are written to `outputs\final\`.

**Important:** the default pipeline renders placeholder visuals, a tonal audio bed, and silent narration. It does not call external generative AI services.