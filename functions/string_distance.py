from functions.word_distance import edit_distance_word

def edit_distance(str1, adict):
    """
    Find the closest word in a dictionary to a given word based on minimum edit distance.

    Args:
        str1 (str): The input word.
        adict (dict): A dictionary containing words as keys.

    Returns:
        str: The word from the dictionary that is closest to the input word based on minimum edit distance.
    """
    mind = float("inf")
    closename = ""
    # m, n = len(str1), len(str2)
    # Iterate through each word in the dictionary
    for name in adict.keys():
        # Calculate the edit distance between the input word and the current word in the dictionary
        result = edit_distance_word(str1, name.lower())
        # Update the minimum edit distance and closest word if necessary
        if result < mind:
            mind = result
            closename = name
    
    return closename