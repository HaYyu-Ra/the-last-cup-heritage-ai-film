"""Render placeholder cards as slow-zoom video clips using FFmpeg."""
import subprocess, time
from .config import ROOT
from .utils import load_storyboard, digest_payload, cached, save_cache_key, log_run, ensure_dirs

def main():
    ensure_dirs(); data=load_storyboard(); outdir=ROOT/"outputs"/"shots"
    for shot in data["shots"]:
        src=ROOT/"outputs"/"keyframes"/(shot["id"]+".png"); out=outdir/(shot["id"]+".mp4")
        key=digest_payload(shot["duration"],src.stat().st_size,"ffmpeg-zoompan-v1")
        if cached(key,out): continue
        fps=12; frames=shot["duration"]*fps; vf=f"scale=480:854,zoompan=z='min(zoom+0.00025,1.08)':d={frames}:s=480x854:fps={fps},format=yuv420p"
        started=time.time(); subprocess.run(["ffmpeg","-y","-loop","1","-i",str(src),"-t",str(shot["duration"]),"-vf",vf,"-r",str(fps),"-an","-c:v","libx264","-preset","ultrafast",str(out)],check=True,capture_output=True)
        save_cache_key(out,key); log_run("shots","FFmpeg zoompan",started,out,"Deterministic fallback animation")
if __name__=="__main__": main()
