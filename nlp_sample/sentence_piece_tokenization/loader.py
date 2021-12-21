from io import BytesIO
from urllib.request import urlopen


def load_text(url: str) -> BytesIO:
    with urlopen(url) as response:
        text = BytesIO(response.read())
    return text
