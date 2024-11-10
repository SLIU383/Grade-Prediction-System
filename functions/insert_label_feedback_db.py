import sqlite3

def clear_db():
    conn = sqlite3.connect('database/feedback_model_prediction.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM feedback')
    conn.commit()
    conn.close()

def insert_assigned_feedback(author, student_id, feedback,label):
    """
    Insert feedback data into the SQLite database.

    Args:
        author (str): The author of the feedback.
        student_id (str): The ID of the student in the team.
        feedback (str): The feedback text.
        label (str): 1 - is feedback, 0 - not feedback.

    Returns:
        None
    """
    conn = sqlite3.connect('database/feedback_model_prediction.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO feedback VALUES (?, ?, ?, ?)', (author, student_id, feedback, label))
    
    conn.commit()
    conn.close()