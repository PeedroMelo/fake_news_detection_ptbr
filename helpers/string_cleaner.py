import re
import unicodedata

class StringCleaner:

    def remove_url(text):
        return re.sub(r'http\S+', '',text)

    def remove_between_square_brackets(text):
        return re.sub('\[[^]]*\]', '', text)

    def remove_special_characters(text):
        return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII")