import json
import os


def load_json(path):
    """
    Safely load JSON.
    Returns {} if file doesn't exist or is invalid.
    """

    if not os.path.exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception as e:

        print(f"⚠ Could not load {path}")
        print(e)

        return {}


def save_json(path, data):
    """
    Safely save JSON.
    """

    os.makedirs(
        os.path.dirname(path),
        exist_ok=True,
    )

    with open(
        path,
        "w",
        encoding="utf-8",
    ) as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False,
        )