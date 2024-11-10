from functions.string_distance import edit_distance
from functions.generate_name_list import generate_name_list

def get_name_variant_dict(text, filename,p_team_name_dic): #get dict of variant of name
    """
    Generate a dictionary of word frequencies and name appearance frequencies from a given text.

    Args:
        text (str): The input text.
        filename (str): The filename from which the text originated.
        p_team_name_dic (dict): A dictionary mapping person names to team names.

    Returns:
        list: A list containing three elements:
              1. Author's name.
              2. List of variants of student names.
              3. A list of proper nouns extracted from the text based on the author's team.
              4. A list of team members
    """
    # get the author name of the text based on the filename
    author = edit_distance(filename.split()[0].split("_")[0],p_team_name_dic)
    team_member = p_team_name_dic[author]
    snl = []
    # Split team member names into individual names
    for item in team_member:
        snl += item.split(", ")
    # Generate a list of variants of student names from the text based on the author's team members
    re_l, group_variant_dict = generate_name_list(text,snl)
    re_l += snl
    re_l = list(set(re_l)) #remove duplicates
    return [author,re_l,group_variant_dict,team_member]