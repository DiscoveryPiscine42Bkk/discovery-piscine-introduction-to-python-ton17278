def average(scores_dict):
    """
    Calculates the average score from a dictionary of student names and scores.
    
    Parameters:
    scores_dict (dict): A dictionary with student names as keys and their scores as values.

    Returns:
    float: The average score.
    """
    if not scores_dict:
        return 0.0
    total_score = sum(scores_dict.values())
    number_of_students = len(scores_dict)
    return total_score / number_of_students



class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}


print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")