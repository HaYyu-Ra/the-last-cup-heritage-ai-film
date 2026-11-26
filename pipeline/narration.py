"""Create a silent narration placeholder; script text is stored in storyboard.json."""
import wave, time
from .config import ROOT
from .utils import load_storyboard, digest_payload, cached, save_cache_key, log_run, ensure_dirs

def main():
    ensure_dirs(); data=load_storyboard(); duration=data["project"]["total_duration_seconds"]; sr=22050; out=ROOT/"outputs"/"audio"/"narration_placeholder.wav"
    script=" ".join(s["narration_am"] for s in data["shots"]); key=digest_payload(script,duration,"silent-placeholder-v1")
    if cached(key,out): return
    started=time.time()
    with wave.open(str(out),"wb") as wf:
        wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
        silence=b"\x00\x00"*sr
        for _ in range(duration): wf.writeframes(silence)
    save_cache_key(out,key); log_run("narration","silent placeholder",started,out,"No speech synthesis is performed")
if __name__=="__main__": main()
