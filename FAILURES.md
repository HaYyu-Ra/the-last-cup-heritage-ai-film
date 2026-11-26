# Failure journal

Record actual blockers as they happen. The rows below are prompts for observation, not claims that these failures occurred.

| Date | Stage | Symptom / evidence | Attempt(s) | Resolution / fallback | Lesson |
|---|---|---|---|---|---|
| Pending | Provider setup | No provider adapters or credentials configured in the starter run | Kept provider calls out of default offline path | Offline placeholder path is explicit; provider integration remains future work | A runnable fallback is better than pretending a provider call succeeded |
| Pending | Video generation | Wan 2.2 has not been run in this repository | Not attempted here | Ken Burns motion from still keyframes is the documented fallback | Do not claim generated video-model clips |
| Pending | Narration | Gemini TTS has not been called | Not attempted here | Amharic text and English subtitles remain in storyboard; generated narration is not present | Validate pronunciation with a fluent speaker before release |
| Pending | Music | ACE-Step has not been called | Not attempted here | Offline tone bed is used only as a placeholder | A tone bed is not an original model-composed score |

## Risks to investigate
- Provider free tiers, API availability and rate limits may change.
- Kaggle/Colab sessions may time out or run out of VRAM.
- Character identity can drift between generated images and clips.
- Amharic TTS pronunciation and prosody need a fluent listener.
- FFmpeg must be installed and available on PATH.
- Generated cultural objects and clothing need review by someone familiar with the tradition.

When a real failure occurs, replace or extend the relevant row with timestamped logs, exact error text (redact secrets), what you tried, and what fixed it.
