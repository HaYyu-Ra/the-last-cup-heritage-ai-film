# AI Workflow and Integration Plan

The project uses a storyboard-first workflow. `storyboard.json` is the shared input contract for production stages.

## Intended workflow
1. Human-reviewed story concept and shot list.
2. Prompt development for each approved shot.
3. Image generation for keyframes.
4. Optional image-to-video motion generation.
5. Amharic narration synthesis and human pronunciation review.
6. Original music creation or properly licensed music selection.
7. Editing, subtitles, quality review, and export.

## Current implementation versus planned AI
| Stage | Current implementation | Planned enhancement |
|---|---|---|
| Story | Human-authored storyboard | Editorial review |
| Visuals | Labeled placeholder cards | Image model adapter |
| Motion | FFmpeg Ken Burns fallback | Image-to-video adapter |
| Music | Synthesized tone placeholder | Licensed/original score |
| Narration | Silent WAV placeholder | Amharic TTS + human review |
| Assembly | FFmpeg exports | Color, subtitle, sound-mix polish |

For real model calls, record provider, model/version, parameters, seed where supported, latency, cost, output path, and status. Never commit API keys; use environment variables and an untracked `.env` file.