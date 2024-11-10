from fuzzywuzzy import fuzz
from nltk.tag import pos_tag
from functions.is_word import is_word
from nltk.tokenize import word_tokenize

def generate_name_list(text, name_list):
    """
    Generate a list of variants of student names which be used in the document eg. Kei - Keisuke.

    Args:
        text (str): The input text from which proper nouns are to be extracted.
        name_list (list): A list of reference names.

    Returns:
        list: a list of variants of student names which be used in the document.
    """
    result_list = []
    name_variants_dict = {}

     # Iterate through each name in the reference name list
    for name in name_list:
        name_variants_dict[name] = []
        # Iterate through each word in the text
        for item in text.split(" "):
            # Check if the word matches the name exactly or has a fuzzy ratio greater than 50% with the name
            if item.lower() == name.lower() or (fuzz.ratio(item.lower(),name.lower()) > 50 and not is_word(item)):
                result_list.append(item)
                name_variants_dict[name].append(item)
    
    text2 = ""
    # Initialize a list to store name
    result_l2 = []
    # Concatenate the matched words into a single string
    for item in result_list:
        text2 += item + " "
    # Tokenize the concatenated text and identify proper nouns
    for (word, pos) in pos_tag(word_tokenize(text2)):
        if pos == 'NNP':
            result_l2.append(word)
    return (result_l2,name_variants_dict)