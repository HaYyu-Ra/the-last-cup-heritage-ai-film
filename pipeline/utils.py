import hashlib, json, time
from .config import ROOT, RUN_LOG

def load_storyboard():
    return json.loads((ROOT / "storyboard.json").read_text(encoding="utf-8"))

def digest_payload(*values):
    return hashlib.sha256(json.dumps(values, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()

def cached(key, output):
    marker = output.with_suffix(output.suffix + ".cachekey")
    return output.exists() and marker.exists() and marker.read_text().strip() == key

def save_cache_key(output, key):
    output.with_suffix(output.suffix + ".cachekey").write_text(key, encoding="utf-8")

def log_run(stage, implementation, started, output, note=""):
    row = {"stage":stage,"implementation":implementation,"latency_seconds":round(time.time()-started,3),"cost_usd":0.0,"status":"success","output":str(output),"note":note}
    with RUN_LOG.open("a",encoding="utf-8") as f: f.write(json.dumps(row,ensure_ascii=False)+"\n")

def ensure_dirs():
    for name in ("keyframes","shots","audio","final","cache"):
        (ROOT / "outputs" / name).mkdir(parents=True, exist_ok=True)
