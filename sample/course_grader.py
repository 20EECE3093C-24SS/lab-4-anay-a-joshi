# Name: Anay Abhijit Joshi
# NOTE: This is taken from the course document (Requirements) - 
# Function Name: The function must be correctly named convert_to_letter_grade.
# Input Argument: It should accept a single parameter named score, representing the student’s numerical score to be converted into a letter grade.
# Output: The function is expected to return an upper-case string indicating the student’s letter grade, determined based on the following score ranges:
# A: 90 to 100
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60

# Invalid Input:
# The function must raise a ValueError with the message “Score must be between 0 and 100.” for input scores outside the 0 to 100 range.
# The function must raise a TypeError with the message “Score must be a numeric value.” if the input score is not an int or float.


# TODO-1: add convert_to_letter_grade(score) function
def convert_to_letter_grade(score):
    """
    Converts a student’s numerical score (int or float) into a corresponding letter grade [A,B,C,D,F]

    Args:
        score (float or int): The numerical score of the student which will get converted into its corresponding letter grade.

    Returns:
        str: An upper-case string indicating the student’s letter grade, determined based on the following score ranges:
                A: 90 to 100
                B: 80 to 89
                C: 70 to 79
                D: 60 to 69
                F: Below 60

    Raises:
        TypeError: If the input `score` of the student is not a numeric value (int or float).
        ValueError: If the input `score` of the student is outside 0 to 100 range.
    """
    
    # Conditional Check to see if the score is a numeric value....
    if not isinstance(score, (float, int)):
        # if not, then raise a TypeError
        raise TypeError("Score must be a numeric value.")
    # Conditional Score range check
    if (score < 0 or score > 100):
        # Raise the ValueError
        raise ValueError("Score must be between 0 and 100.")
    # Match the grades with the score(s) of the students
    # Return upper-case string
    # Below 60
    if (score < 60):
        return ("f".upper())
        #return "F"    # another approach to do so
    # Below 70 and above 60
    elif score < 70:
        return ("d".upper())
        #return "D"    # another approach to do so
    # Below 80 and above 70
    elif score < 80:
        return ("c".upper())
        #return "C"    # another approach to do so
    # Below 90 and above 80
    elif score < 90:
        return ("b".upper())
        #return "B"    # another approach to do so
    # Below 100 and above 90
    else:
        return ("a".upper())
        #return "A"    # another approach to do so
