# The Last Cup — Ethiopian Heritage Short Film

A 75-second cinematic tribute to Ethiopia's coffee ceremony, family, hospitality, and intergenerational memory.

## Amharic cinematic edition

The production workflow now uses:
- A generated nine-scene Ethiopian coffee-ceremony image montage, split into individual scene frames.
- Amharic narration synthesized from the reviewed script with Google Text-to-Speech (gTTS, language `am`).
- An original, procedurally synthesized pentatonic-inspired instrumental accompaniment. It is an original electronic score, **not** a field recording or a claim of authentic traditional performance.
- Gentle Ken Burns motion and vertical (9:16) plus horizontal (16:9) H.264/AAC exports.
- GitHub Actions validation of audio streams and downloadable MP4 artifacts.

## Build locally (Windows PowerShell)

Requirements: Python 3.11+, FFmpeg on PATH, and internet access for Amharic speech synthesis.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pipeline.validate
python -m pipeline.production
```

Outputs:
- `outputs/final/the_last_cup_vertical.mp4`
- `outputs/final/the_last_cup_horizontal.mp4`
- `outputs/audio/amharic_narration.mp3`
- `outputs/audio/original_instrumental.wav`

## GitHub Actions

Push changes to `assets/**`, `pipeline/production.py`, or `requirements.txt`, or manually run **Render The Last Cup — Amharic cinematic edition** from Actions. Download the artifact named `the-last-cup-amharic-cinematic`.

## Narration script

ቡና ለኢትዮጵያውያን ከመጠጥ በላይ ትርጉም አለው። ቡና የታሪካችን፣ የባህላችንና የአንድነታችን ምልክት ነው።

ከቡና ፍሬ መታጠብ፣ መቆላትና መፍጨት ጀምሮ፣ በገንቦ ውስጥ እስከሚፈላበት ድረስ፣ እያንዳንዱ ሂደት የራሱ ውበት አለው።

የቡና ሥነ ሥርዓት ቤተሰብን ያሰባስባል፣ ጎረቤትን ያቀራርባል፣ ወዳጅነትንም ያጠናክራል።

ዛሬ የምንጠጣው ቡና የትናንቱን ታሪክ ይዞ ወደ ነገ ይጓዛል።

ባህላችንን እንጠብቅ። ታሪካችንን ለትውልድ እናስተላልፍ።

ኢትዮጵያዊነት በአንድ ጽዋ ቡና ውስጥ!

## Honest production note

The images are AI-generated illustrative visuals. The voice is TTS, not a human family recording. The instrumental track is algorithmically synthesized. Review the Amharic pronunciation and cultural details before public release. The speech-synthesis step requires network access.
