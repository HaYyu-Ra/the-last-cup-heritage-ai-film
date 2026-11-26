"""Synthesize a simple tonal placeholder bed, not a composed music track."""
import wave, math, struct, time
from .config import ROOT
from .utils import load_storyboard, digest_payload, cached, save_cache_key, log_run, ensure_dirs

def main():
    ensure_dirs(); data=load_storyboard(); duration=data["project"]["total_duration_seconds"]; sr=22050; out=ROOT/"outputs"/"audio"/"music_placeholder.wav"
    key=digest_payload(data["music"],duration,"tone-placeholder-v1")
    if cached(key,out): return
    started=time.time(); volume=float(data["music"].get("volume",0.12)); notes=(110.0,146.83,164.81)
    with wave.open(str(out),"wb") as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
        for start in range(0,duration*sr,4096):
            buf=[]
            for n in range(min(4096,duration*sr-start)):
                t=(start+n)/sr; fade=min(1,t/2,(duration-t)/2); sample=sum(math.sin(2*math.pi*f*t) for f in notes)/9*volume*max(0,fade)
                buf.append(struct.pack("<h",int(max(-1,min(1,sample))*32767)))
            wf.writeframes(b"".join(buf))
    save_cache_key(out,key); log_run("music","synthesized tone placeholder",started,out,"Not an AI-generated or culturally authentic musical score")
if __name__=="__main__": main()
