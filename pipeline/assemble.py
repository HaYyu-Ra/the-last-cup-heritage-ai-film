"""Concatenate shot clips and export 9:16 and 16:9 versions with placeholder audio."""
import subprocess, time
from .config import ROOT
from .utils import load_storyboard, ensure_dirs, log_run

def run(cmd): subprocess.run(cmd,check=True,capture_output=True,text=True)

def main():
    ensure_dirs(); data=load_storyboard(); tmp=ROOT/"outputs"/"tmp"; tmp.mkdir(parents=True,exist_ok=True)
    concat=tmp/"clips.txt"
    with concat.open("w",encoding="utf-8") as f:
        for shot in data["shots"]:
            p=ROOT/"outputs"/"shots"/(shot["id"]+".mp4"); f.write("file '"+str(p).replace("'","'\\''")+"'\n")
    silent=tmp/"video.mp4"; started=time.time(); run(["ffmpeg","-y","-f","concat","-safe","0","-i",str(concat),"-c","copy",str(silent)])
    audio=ROOT/"outputs"/"audio"/"music_placeholder.wav"; outputs=ROOT/"outputs"/"final"
    for label,size in (("vertical","1080:1920"),("horizontal","1920:1080")):
        out=outputs/("the_last_cup_"+label+".mp4"); vf=f"scale={size}:force_original_aspect_ratio=increase,crop={size},setsar=1,fps=24"
        run(["ffmpeg","-y","-i",str(silent),"-i",str(audio),"-vf",vf,"-map","0:v","-map","1:a","-c:v","libx264","-preset","ultrafast","-crf","27","-c:a","aac","-shortest",str(out)])
    log_run("assemble","FFmpeg",started,outputs,"Exports contain placeholder imagery and tone-bed audio; narration remains silent")
if __name__=="__main__": main()
