from functions.remove_symbol import remove_symbols

def coreference_resolution(text, name_l):
    """
    Resolve coreferences in a given text.

    Args:
        text (str): The input text.
        name_l (list): A list of names.

    Returns:
        str: The input text with coreferences resolved.
    """
    # expand name list by adding students' first and last name
    nl = []
    for item in name_l:
        nl += item.split(", ")

    entities = {} 
    doc = text.split(" ")
    pr = ["he","she","they","him","his","her"] #pronouns
    ind = 0 #word index
    name_distance = 0
    name = ""
    for token in doc:
        token = remove_symbols(token)
        tokenIsName = False
        # for item in nl:
        #     if(edit_distance_word(token,item) <= 1):
        #         tokenIsName = True
        if(token in nl):
            if(name_distance <= 2):
                name += " " + token 
            else:
                name = token
            name_distance = 0
        # print(token.sent)
        if token.lower() in pr:
            if name != "":
                entities[ind] = name
        if token.lower() in ["they", "them", "their"] and len(name.split(" ")) >= 2:
            entities[ind] = name
        # if token.lower() == "team":
        #     name = ", ".join(nl)
        name_distance += 1
        ind += 1
    ind2 = 0
    resolved_text = ""
    for token in doc:
        if ind2 in entities.keys():
            resolved_text += entities[ind2] + " "
        else:
            resolved_text += token + " "
        ind2 += 1
    
    return resolved_text.strip()