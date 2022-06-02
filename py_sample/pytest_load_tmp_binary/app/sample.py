import pickle
from pathlib import Path

def load_binary(filepath: Path) -> str:
    with open(filepath, "rb") as f:
        text = pickle.load(f)
    return text
