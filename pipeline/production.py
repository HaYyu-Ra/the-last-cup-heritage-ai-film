"""Cinematic renderer: 9 generated coffee-ceremony images + Amharic speech + original score."""
import math, os, subprocess, wave
from pathlib import Path
from PIL import Image
from gtts import gTTS

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"
SCRIPT="""ቡና ለኢትዮጵያውያን ከመጠጥ በላይ ትርጉም አለው። ቡና የታሪካችን፣ የባህላችንና የአንድነታችን ምልክት ነው።
ከቡና ፍሬ መታጠብ፣ መቆላትና መፍጨት ጀምሮ፣ በገንቦ ውስጥ እስከሚፈላበት ድረስ፣ እያንዳንዱ ሂደት የራሱ ውበት አለው።
የቡና ሥነ ሥርዓት ቤተሰብን ያሰባስባል፣ ጎረቤትን ያቀራርባል፣ ወዳጅነትንም ያጠናክራል።
ዛሬ የምንጠጣው ቡና የትናንቱን ታሪክ ይዞ ወደ ነገ ይጓዛል።
ባህላችንን እንጠብቅ። ታሪካችንን ለትውልድ እናስተላልፍ።
ኢትዮጵያዊነት በአንድ ጽዋ ቡና ውስጥ!"""

def run(args): subprocess.run(args,check=True)
def score(path,secs=75):
    sr=44100; notes=[220.0,261.63,293.66,329.63,392.0]
    with wave.open(str(path),"wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        for start in range(0,secs*sr,4096):
            data=bytearray()
            for i in range(start,min(start+4096,secs*sr)):
                t=i/sr; f=notes[int(t*.75)%5]; phase=(t*f)%1
                pluck=math.exp(-5*phase)*math.sin(2*math.pi*f*t)
                pulse=.18*math.sin(2*math.pi*110*t)*(1 if t%0.667<.09 else .15)
                fade=min(1,t/3,(secs-t)/4); v=max(-.7,min(.7,(.13*pluck+.22*pulse)*max(0,fade)))
                b=int(v*32767).to_bytes(2,"little",signed=True); data.extend(b+b)
            w.writeframes(data)

def main():
    (OUT/"audio").mkdir(parents=True,exist_ok=True); (OUT/"final").mkdir(parents=True,exist_ok=True)
    collage=Image.open(ROOT/"assets/coffee_ceremony_collage.jpg").convert("RGB")
    sw,sh=collage.size; imgs=[]
    for r in range(3):
        for c in range(3):
            p=OUT/"tmp"/f"scene_{r*3+c+1:02d}.jpg"; p.parent.mkdir(parents=True,exist_ok=True)
            collage.crop((round(c*sw/3),round(r*sh/3),round((c+1)*sw/3),round((r+1)*sh/3))).save(p,quality=94)
            imgs.append(p)
    speech=OUT/"audio/amharic_narration.mp3"; music=OUT/"audio/original_instrumental.wav"
    gTTS(text=SCRIPT,lang="am",slow=False).save(str(speech)); score(music)
    for name,w,h in [("vertical",1080,1920),("horizontal",1920,1080)]:
        folder=OUT/"tmp"/name; folder.mkdir(parents=True,exist_ok=True); clips=[]
        for n,img in enumerate(imgs):
            clip=folder/f"{n:02d}.mp4"; clips.append(clip)
            vf=f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},zoompan=z='min(zoom+0.0007,1.06)':d=200:s={w}x{h}:fps=24,fade=t=in:st=0:d=0.4,format=yuv420p"
            run(["ffmpeg","-y","-loop","1","-i",str(img),"-t","8.333","-vf",vf,"-an","-c:v","libx264","-preset","ultrafast","-crf","24",str(clip)])
        listing=folder/"list.txt"; listing.write_text("".join(f"file '{p.resolve()}'\n" for p in clips),encoding="utf-8")
        picture=folder/"picture.mp4"; run(["ffmpeg","-y","-f","concat","-safe","0","-i",str(listing),"-c","copy",str(picture)])
        dest=OUT/"final"/f"the_last_cup_{name}.mp4"
        run(["ffmpeg","-y","-i",str(picture),"-i",str(speech),"-i",str(music),"-filter_complex","[1:a]volume=1[n];[2:a]volume=.20[m];[n][m]amix=inputs=2:duration=longest:dropout_transition=2,alimiter=limit=.95[a]","-map","0:v","-map","[a]","-t","75","-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart",str(dest)])
    (OUT/"audio/amharic_narration.txt").write_text(SCRIPT,encoding="utf-8")
    print("SUCCESS: both MP4s include audible Amharic narration and original synthesized instrumental music.")
if __name__=="__main__": main()
