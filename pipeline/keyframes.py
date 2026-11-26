"""Create labeled offline placeholder keyframe cards; no image model is called."""
import time, textwrap
from PIL import Image, ImageDraw, ImageFont
from .config import ROOT
from .utils import load_storyboard, digest_payload, cached, save_cache_key, log_run, ensure_dirs

def main():
    ensure_dirs(); data=load_storyboard(); outdir=ROOT/"outputs"/"keyframes"
    for shot in data["shots"]:
        out=outdir/(shot["id"]+".png"); key=digest_payload(shot.get("image_prompt"),shot.get("subtitle_en"),"offline-card-v1")
        if cached(key,out): continue
        img=Image.new("RGB",(720,1280),(48,37,27)); draw=ImageDraw.Draw(img)
        try: font=ImageFont.truetype("DejaVuSans.ttf",25)
        except OSError: font=ImageFont.load_default()
        draw.rounded_rectangle((35,35,685,1245),radius=24,outline=(190,151,91),width=3)
        draw.text((70,100),shot["id"].upper(),font=font,fill=(245,218,170))
        y=300
        for line in textwrap.wrap(shot["image_prompt"],42): draw.text((70,y),line,font=font,fill=(240,230,210)); y+=42
        draw.text((70,1050),"OFFLINE PLACEHOLDER — NOT AI GENERATED",font=font,fill=(255,190,100))
        for line in textwrap.wrap(shot["subtitle_en"],42): y+=38; draw.text((70,y),line,font=font,fill="white")
        started=time.time(); img.save(out); save_cache_key(out,key); log_run("keyframes","Pillow placeholder card",started,out,"Replace with an image-generation adapter for real AI imagery")
        print("[keyframes]",shot["id"])
if __name__=="__main__": main()
