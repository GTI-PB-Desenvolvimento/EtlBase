import re
from unidecode import unidecode


def structure_text(text: str) -> str:
    return re.sub(r'[^A-Z\s]','',unidecode(text.upper()).strip()) if text else ''
