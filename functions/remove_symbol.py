import re

def remove_symbols(sentence):
    """
    Remove non-alphabetic characters, except for whitespaces and periods, from a given sentence.

    Args:
        sentence (str): The input sentence containing symbols to be removed.

    Returns:
        str: A cleaned version of the input sentence with non-alphabetic characters removed, 
             except for whitespaces and periods. Additionally, replaces '?' with '.' 
             and removes any newline characters by replacing them with whitespaces.
    """
    # Define regex pattern to match non-alphabetic characters, except whitespaces and periods
    pattern = r'[^a-zA-Z\s\.]'

    # Replace non-alphabetic characters with an empty string
    clean_sentence = re.sub(pattern, '', sentence)

    # Replace '?' with '.'
    clean_sentence2 = re.sub(r'\?', '.', clean_sentence)

    # Replace newline characters with whitespaces
    for index in range(len(clean_sentence2)):
        if(clean_sentence2[index] == "\n"):
            clean_sentence2 = clean_sentence2[:index] + " " + clean_sentence2[index+1:]
    return clean_sentence2