"""Run the pipeline stages in order, retrying transient stage failures."""
import os
import subprocess
import sys
import time
from .config import ROOT

MAX_ATTEMPTS = max(1, int(os.getenv("PIPELINE_RETRIES", "2")))

def stage(module):
    print(f"\n=== {module} ===", flush=True)
    command = [sys.executable, "-m", f"pipeline.{module}"]
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            subprocess.run(command, cwd=ROOT, check=True)
            return
        except subprocess.CalledProcessError:
            if attempt == MAX_ATTEMPTS:
                raise
            delay = min(2 ** (attempt - 1), 8)
            print(f"[retry] {module} failed on attempt {attempt}; retrying in {delay}s", flush=True)
            time.sleep(delay)

def main():
    for module in ("validate", "keyframes", "shots", "music", "narration", "assemble"):
        stage(module)
    print("\nPipeline finished. Default keyframes, music and narration are offline placeholders, not real model outputs.")

if __name__ == "__main__":
    main()
