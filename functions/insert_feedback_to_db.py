import sqlite3

def clear_db():
    conn = sqlite3.connect('database/coreference_origin_text.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM feedback')
    conn.commit()
    conn.close()

def insert_feedback(pdf_name, pdf_content):
    """
    Insert feedback data into the SQLite database.

    Args:
        pdf_name (str): The name of the reflection document.
        pdf_content (str): The content of corresponding reflection document.

    Returns:
        None
    """
    conn = sqlite3.connect('database/coreference_origin_text.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO feedback VALUES (?, ?)', (pdf_name, pdf_content))
    
    conn.commit()
    conn.close()