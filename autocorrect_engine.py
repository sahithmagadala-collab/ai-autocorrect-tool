from textblob import TextBlob
import re

def correct_text(text):

    # Correct full sentence using TextBlob
    blob = TextBlob(text)

    corrected_text = str(blob.correct())

    # Capitalize first letter properly
    corrected_text = corrected_text.capitalize()

    return corrected_text