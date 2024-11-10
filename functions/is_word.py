
from nltk.corpus import wordnet

def is_word(word):
    """
    Check if a given string is a valid word.

    Args:
        word (str): The input string to be checked.

    Returns:
        bool: True if the input string is a valid word, False otherwise.
    """
    synsets = wordnet.synsets(word)
    for synset in synsets:
        # Check if synset is a noun, verb, adjective, adverb, or interjection
        if synset.pos() in ['v', 'n', 'a', 'r', 'i']:
            return True
    return False