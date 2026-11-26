# Costs and measurements

## Measurement status
The current default run is **offline and uses placeholders**. It does not call FLUX, Wan, Gemini TTS, or ACE-Step. Local stage timings are written to `runs.jsonl`; rerun on your machine to capture your hardware-specific measurements.

| Stage | Current implementation | Latency | GPU minutes | Provider cost | Status |
|---|---|---:|---:|---:|---|
| Validation | Python + jsonschema | See runs.jsonl | 0 | $0 | Local |
| Keyframes | Pillow placeholder cards | See runs.jsonl | 0 | $0 | Not AI image generation |
| Moving shots | FFmpeg Ken Burns animation | See runs.jsonl | 0 | $0 | Not Wan |
| Music | Offline tone placeholder | See runs.jsonl | 0 | $0 | Not ACE-Step composition |
| Narration | Silent WAV placeholder | See runs.jsonl | 0 | $0 | Not Gemini TTS |
| Assembly | FFmpeg | See runs.jsonl | 0 | $0 | Local render |

## Interpreting cost
The current offline path has no provider charges. This is not a list-price comparison for hosted AI models. For every future provider call, log the exact model/version, parameters, seed, wall latency, GPU minutes where applicable, usage quantity, list-price-equivalent estimate, and actual charged amount (if any).

## Reproduction
Run `python -m pipeline.run` and inspect the appended JSONL records. Do not copy timings from another machine as if they were yours. No frontier-model comparison has been performed in this repository.
