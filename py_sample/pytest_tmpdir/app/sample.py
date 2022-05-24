from typing import List

from pathlib import Path


def load_texts(file_dir: Path) -> str:
    texts = "".join([
        file.read_text() for file in sorted(file_dir.iterdir())
    ])
    return texts
