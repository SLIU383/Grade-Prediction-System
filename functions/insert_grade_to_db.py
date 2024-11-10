import sqlite3

def clear_db():
    conn = sqlite3.connect('database/student_grade.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM feedback')
    conn.commit()
    conn.close()

def insert_grade(student_name, student_grade):
    """
    Insert feedback data into the SQLite database.

    Args:
        student_name (str): The student name.
        student_grade (str): The suggested grade of the corresponding student.

    Returns:
        None
    """
    conn = sqlite3.connect('database/student_grade.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO feedback VALUES (?, ?)', (student_name, student_grade))
    
    conn.commit()
    conn.close()