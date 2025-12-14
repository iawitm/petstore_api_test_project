import json
from pathlib import Path

from helpers.path_helper import resource_path


def load_json(json_name):
    json_path = resource_path("json_api", json_name)
    with open(json_path, encoding="utf-8") as f:
        loaded_json = json.load(f)

    return loaded_json