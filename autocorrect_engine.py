from spellchecker import SpellChecker
import re

spell = SpellChecker()

def correct_text(text):

    words = re.findall(r'\w+|\s+|[^\w\s]', text)

    corrected_words = []

    for word in words:

        if word.isalpha():

            corrected_word = spell.correction(word)

            corrected_words.append(corrected_word)

        else:
            corrected_words.append(word)

    corrected_sentence = "".join(corrected_words)

    return corrected_sentence