from functions.preprocess_text import preprocess_text
from functions.get_name_dict import get_name_dict

def split_into_diff_student(pdf_file_name, author,full_name_list, group_variant_dict, name_l, coref_text, all_origin_content_dict):
    """
    Splits feedback content in a document by student names and associates each section of feedback 
    with the corresponding student.

    Parameters:
    pdf_file_name (str): The name of the PDF file containing feedback.
    author (str): The author of the document.
    full_name_list (list): A list of full names of students in the group.
    group_variant_dict (dict): A dictionary of name variants for each group member.
    name_l (list): A list of first names or nickname variations to search in the text.
    coref_text (str): The coreference-resolved text content, where pronouns are replaced by names.
    all_origin_content_dict (dict): A dictionary with the original content of each document.

    Returns:
    dict: A dictionary where each key is a student name, and the value is a list of feedback 
          sentences associated with that student.
    """
    result_dict = {}
    convert_dict = get_name_dict(full_name_list, group_variant_dict, name_l)
    for item in coref_text.split("."):
        for name in name_l:
            if name in item:
                for key in convert_dict.keys():
                    if name in convert_dict[key]:
                        if key in result_dict:
                            print(item)
                            if(not item in result_dict[key]):
                                print("True")
                                result_dict[key].append(item)
                        else:
                            result_dict[key] = [item]
    for name in name_l:
        for key in convert_dict.keys():
            if name in convert_dict[key]:
                if key not in result_dict.keys():
                    # result_dict[key] = ["No feedback"]
                    result_dict[key] = []
                    for item in all_origin_content_dict[pdf_file_name]:
                        for name_part in convert_dict[key]:
                            if name_part in item:
                                result_dict[key].append(preprocess_text(item))

                    if(result_dict[key] == []):
                        result_dict[key] = ["No Corresponding Name in Reflection"]
    return result_dict