import re
import unicodedata

class StringCleaner:

    def remove_url(text):
        return re.sub(r'http\S+', '',text)

    def remove_special_characters(text):
        text = text.replace('-', ' ')
        text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII")
        return re.sub('[^a-zA-Z0-9 \\\]', '', text)
        