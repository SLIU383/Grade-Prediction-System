import sqlite3
from functions.preprocess_text import preprocess_text
from functions.predict_feedback import predict_sentences
from functions.split_feedback_in_student import split_into_diff_student
from functions.insert_assigned_feedback_db import insert_assigned_feedback, clear_db
from functions.get_variant_name import get_name_variant_dict


def extract_feedback_process(person_team_name_dic):
    conn = sqlite3.connect('database/coreference_origin_text.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM feedback")

    # Fetch the results
    rows = cursor.fetchall()

    test_content = []
    origin_content = []
    pdf_name = []
    # Iterate over the results
    for row in rows:
        pdf_name.append(row[0])
        origin_content.append(row[1])
        test_content.append(preprocess_text(row[1]))

    # Close the connection
    conn.close()

    predictor = predict_sentences('trained_models/feedback_extraction.pth')
    all_preds = predictor.predict_sentences(test_content)

    content_dict = {}

    for index in range(len(pdf_name)):
        _pdf_name = pdf_name[index]
        if(_pdf_name not in content_dict.keys()):
            content_dict[_pdf_name] = [origin_content[index]]
        else:
            content_dict[_pdf_name].append(origin_content[index])

    for key in content_dict.keys():
        ct = content_dict[key]
        result = []
        for item in ct:
            for item2 in item.split("."):
                result.append(item2)
        content_dict[key] = set(result)

    pdf_dict = {}
    for i in range(len(all_preds)):
        if(all_preds[i] == 1):
            if pdf_name[i] in pdf_dict:
                pdf_dict[pdf_name[i]].append(origin_content[i])
            else:
                pdf_dict[pdf_name[i]] = [origin_content[i]]

    new_s = []
    for key in pdf_dict.keys():
        for item in pdf_dict[key]:
            print(item)
            for item2 in item.split("."):
                if item2.strip() not in new_s:
                    new_s.append(item2.strip())
        break

    combine_dict = {}

    for item in pdf_dict.keys():
        nl = []
        for para in (pdf_dict[item]):
            for item2 in para.split("."):
                if item2.strip() not in nl:
                    nl.append(item2.strip())
        combine_dict[item] = ". ".join(nl)


    clear_db()
    for pdf_file_name in combine_dict.keys():
        paragraph = combine_dict[pdf_file_name]
        author,name_l,gvd,team_member_full_name_list = get_name_variant_dict(paragraph, pdf_file_name, person_team_name_dic)
        name_l += team_member_full_name_list
        for item in team_member_full_name_list:
            name_l += item.split(", ")
        fb_dict = split_into_diff_student(pdf_file_name, author, team_member_full_name_list, gvd, name_l, paragraph, content_dict)
        for key in fb_dict.keys():
            insert_assigned_feedback(author, key, ".".join(fb_dict[key]))

            