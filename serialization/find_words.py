import re

def find_words(text):
    pattern = r'\b\w+\b'
    words = re.findall(pattern, text)

    return words