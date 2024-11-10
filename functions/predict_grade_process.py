import sqlite3
from functions.predict_grade import predict_grade
from functions.insert_grade_to_db import insert_grade, clear_db
from functions.convert_to_text_grade import convert_to_text_grade
from functions.predict_feedback_grade import predict_sentences

def predict_grade_process():
    conn = sqlite3.connect('database/feedback_model_prediction.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM feedback")

    # Fetch the results
    rows = cursor.fetchall()

    author_l = []
    assign_stu_l = []
    feedback_l = []
    label_l = []
    result_l = []
    # Iterate over the results
    for row in rows:
        author_l.append(row[0])
        assign_stu_l.append(row[1])
        feedback_l.append(row[2])
        label_l.append(row[3])
        result_l.append([row[0], row[1], row[2], row[3]])

    # Close the connection
    conn.close()

    student_name_list = sorted(set(assign_stu_l))

    au_dict = {} # sentiment label dict
    fs_dict = {} # feedback dict
    for index in range(len(author_l)):
        if(author_l[index] not in au_dict.keys()):
            au_dict[author_l[index]] = []
            fs_dict[author_l[index]] = []
            for index2 in range(len(assign_stu_l)):
                if(assign_stu_l[index2] == author_l[index]):
                    au_dict[author_l[index]].append(int(label_l[index2]))
                    fs_dict[author_l[index]].append(feedback_l[index2])

    _feedback = [] # feature 1
    _feedback_label = [] # feature 2
    _student_name = {}
    for key in student_name_list:
        if key in fs_dict.keys():
            _feedback.append(fs_dict[key])
            _feedback_label.append(au_dict[key])
            _student_name[key] = [fs_dict[key], au_dict[key]]

    clear_db()
    predictor = predict_sentences('trained_models/grade_prediction.pth')
    for key in student_name_list:
        try:
            all_pred = predictor.predict_grade(_student_name[key][0],_student_name[key][1])
            insert_grade(key, all_pred)
        except:
            insert_grade(key, "No Grade")
