from pathlib import Path

def load_txt(filepath: Path) -> str:
    with open(filepath, "rt") as f:
        text = f.read()    
    return text
