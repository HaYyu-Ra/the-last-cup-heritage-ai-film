"""Remove generated outputs while preserving the output directory."""
import shutil
from pathlib import Path
from .config import ROOT

def main():
    outputs = ROOT / "outputs"
    if outputs.exists():
        for child in outputs.iterdir():
            if child.name == ".gitkeep":
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    outputs.mkdir(exist_ok=True)
    print("[clean] generated outputs removed")

if __name__ == "__main__":
    main()
