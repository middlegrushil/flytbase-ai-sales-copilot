import json
from pathlib import Path


def load_json(path):
    path = Path(path)

    if not path.exists():
        return {}

    with open(path, "r") as f:
        return json.load(f)


def save_json(path, data):
    path = Path(path)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def load_markdown(path):
    path = Path(path)

    if not path.exists():
        return ""

    with open(path, "r") as f:
        return f.read()


def save_markdown(path, text):
    path = Path(path)

    with open(path, "w") as f:
        f.write(text)