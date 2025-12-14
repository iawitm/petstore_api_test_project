import json
from pathlib import Path

def load_json(json_name):
    with open(Path(f"resources/json_api/{json_name}"), encoding="utf-8") as f:
        loaded_json = json.load(f)

    return loaded_json