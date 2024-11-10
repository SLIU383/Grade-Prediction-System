from functions.clean_text import clean_text
from functions.remove_stop_word import remove_stop_words

def preprocess_text(text):
    """
    Preprocess a given text.

    Args:
        text (str): The text to preprocess.

    Returns:
        str: The preprocessed text.
    """
    # Convert the text to lowercase
    text = text.lower()

    remove_s = clean_text(text)

    remove_sw = remove_stop_words(remove_s)

    return remove_sw