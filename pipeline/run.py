import subprocess, sys
from .config import ROOT

def main():
    for module in ("validate", "keyframes", "shots", "music", "narration", "assemble"):
        print(f"\n=== {module} ===", flush=True)
        subprocess.run([sys.executable, "-m", f"pipeline.{module}"], cwd=ROOT, check=True)
    print("\nPipeline finished. Default media assets are offline placeholders, not real model outputs.")

if __name__ == "__main__":
    main()
