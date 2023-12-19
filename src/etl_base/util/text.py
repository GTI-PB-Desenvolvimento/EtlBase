import re
from unidecode import unidecode


class TextUtils:

    @staticmethod
    def structure_text(text: str) -> str:
        if text:
            return re.sub(r'[^A-Z\s]','',unidecode(text.upper()).strip())

        return ''
