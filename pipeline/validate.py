import json
from jsonschema import validate, ValidationError
from .config import ROOT

def main():
    data = json.loads((ROOT / "storyboard.json").read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "schema" / "storyboard.schema.json").read_text(encoding="utf-8"))
    try:
        validate(data, schema)
        total = sum(s["duration"] for s in data["shots"])
        if total != data["project"]["total_duration_seconds"]:
            raise ValueError(f"Shot duration sum {total}s differs from project total")
        print(f"[validate] OK: {len(data['shots'])} shots, {total}s")
    except (ValidationError, ValueError) as exc:
        print(f"[validate] ERROR: {exc}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
