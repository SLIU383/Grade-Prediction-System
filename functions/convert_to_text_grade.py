def convert_to_text_grade(grade):
    """
    Convert a numerical grade to a letter grade based on predefined ranges.
    
    Parameters:
    grade (int): An integer representing the numerical grade.
    
    Returns:
    str: A string representing the letter grade ("A", "B", "C", or "D").
    """
    if grade == 0 or grade == 1 or grade == 2:
        return "A"
    elif grade == 3 or grade == 4 or grade == 5:
        return "B"
    elif grade == 6 or grade == 7 or grade == 8:
        return "C"
    else:
        return "D"