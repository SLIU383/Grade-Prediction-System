def get_name_dict(full_name_list, group_variant_dict, name_l):
    """
    Generate a dictionary of name variants.

    Args:
        full_name_list (list): A list of full names.
        group_variant_dict (dict): A dictionary mapping group members to their variants.
        name_l (list): A list of names.

    Returns:
        dict: A dictionary of name variants.
    """
    name_dict = {}
    for item in full_name_list:
        name_dict[item] = []
    
    for item in name_l:
        for key in name_dict.keys():
            if item in key:
                name_dict[key].append(item)

    return name_dict