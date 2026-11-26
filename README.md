# The Last Cup — Ethiopian Heritage Short Film

A 75-second heritage short inspired by the Ethiopian coffee ceremony. The story explores family, memory, belonging, and traditions carried between generations.

> **Implementation disclosure:** This repository is an offline production-pipeline prototype. Its scene cards, synthesized tone-bed soundtrack, and silent narration track are placeholders—not outputs from AI image, video, music, or speech models. Amharic narration text and English subtitles are included in the storyboard.

## Film details
- Duration: 75 seconds
- Shots: 10
- Languages: Amharic narration text; English subtitles
- Exports: 9:16 vertical and 16:9 horizontal MP4

## Pipeline
1. Validate storyboard against JSON Schema and check total runtime.
2. Create labeled offline placeholder keyframe cards.
3. Render draft motion clips with FFmpeg Ken Burns-style movement.
4. Synthesize a tonal placeholder audio bed.
5. Create a silent narration placeholder; retain Amharic script in the storyboard.
6. Assemble vertical and horizontal MP4 exports.
7. Log stage metadata, latency, implementation labels, and costs.

## Windows quick start
Requirements: Python 3.11+ and FFmpeg available on PATH.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pipeline.validate
python -m pipeline.run
```

See WINDOWS_INSTALL.md for full instructions.

## Outputs
- outputs/keyframes/ — placeholder storyboard cards
- outputs/shots/ — rendered shot clips
- outputs/audio/ — placeholder score and silent narration WAV
- outputs/final/the_last_cup_vertical.mp4
- outputs/final/the_last_cup_horizontal.mp4

Generated media is created locally and is not committed by default.

## Documentation
See ARCHITECTURE.md, ETHICS.md, and docs/ for production workflow and limitations.

## AI integration roadmap
Future work: connect an image-generation provider for keyframes, an image-to-video provider, Amharic text-to-speech, and an original/licensed score. Verify current API access, model licenses, terms, costs, and data handling before use. Never label placeholder assets as AI-generated.

## Responsible storytelling
Use fictional or consenting people, avoid uploading private family information, and review cultural details for accuracy. Disclose generated, edited, recorded, stock, and placeholder assets honestly.

**Project status:** Functional offline pipeline prototype; real generative-model integrations, voiced narration, original score, and final cinematic imagery remain future production tasks.

*Culture lives in the stories we pass on — and the traditions we keep alive.*

## Assignment evidence and report
- `DESIGN.md`: audience, intent, and honest placeholders for both required user tests.
- `EXPERIMENTS.md`: ten hypotheses to test; entries are pending until real evidence is recorded.
- `FAILURES.md`: current implementation limits and a journal for actual blockers.
- `COSTS.md`: measured local run data and clear separation from model/API costs.
- `ETHICS.md`: consent, privacy, disclosure, and licence audit.
- `REPORT_TEMPLATE.md`: Assignment 1 report structure.
- `WALKTHROUGH_PLAN.md`: guide for the required five-minute-or-less recording.
- `PUBLIC_POST_TEMPLATE.md`: starting point for your own public post.
- `runs.jsonl`: measured offline pipeline run; records identify placeholder stages explicitly.

The documentation does not claim that the audience tests, model integrations, ten experiments, public post, or walkthrough have been completed. Those require real participants, provider access, and your own publication/recording.
