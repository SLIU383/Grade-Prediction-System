import sqlite3
from functions.predict_feedback import predict_sentences
from functions.insert_label_feedback_db import insert_assigned_feedback, clear_db

def sentiment_analysis_process():
    conn = sqlite3.connect('database/assigned_feedback.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM feedback")

    # Fetch the results
    rows = cursor.fetchall()

    author_l = []
    feedback_p = []
    assign_stu_l = []

    # Iterate over the results
    for row in rows:
        author_l.append(row[0])
        assign_stu_l.append(row[1])
        feedback_p.append(row[2])

    # Close the connection
    conn.close()
    clear_db()
    predictor = predict_sentences("trained_models/sentiment_analysis.pth")
    feedback_dict = {}
    for index in range(len(author_l)):
        feedback_sentence = feedback_p[index].split(".")
        feedback_dict[author_l[index]] = feedback_sentence

        all_preds = predictor.predict_sentences(feedback_sentence)
        for index2 in range(len(all_preds)):
            all_preds[index2] = str(all_preds[index2])
        if(feedback_p[index] != "No Corresponding Name in Reflection"):
            for index3 in range(len(feedback_sentence)):
                insert_assigned_feedback(author_l[index],assign_stu_l[index],feedback_sentence[index3],all_preds[index3])