# Name: Anay A. Joshi
# Task 3: Grade Conversion Unit Tests

import pytest
from course_grader import convert_to_letter_grade

# NOTE (from Google Python Style Guide) - 
# Module-level docstrings for test files are not required. They should be included only when there is additional information that can be provided.

# TODO-1: Add test_exact_grade_boundaries() function
def test_exact_grade_boundaries():
    # Contains a total of 9 test cases as per the requirement
    assert convert_to_letter_grade(0) == ("f".upper())
    assert convert_to_letter_grade(59) == ("f".upper())
    assert convert_to_letter_grade(60) == ("d".upper())
    assert convert_to_letter_grade(69) == ("d".upper())
    assert convert_to_letter_grade(70) == ("c".upper())
    assert convert_to_letter_grade(80) == ("b".upper())
    assert convert_to_letter_grade(89) == ("b".upper())
    assert convert_to_letter_grade(90) == ("a".upper())
    assert convert_to_letter_grade(100) == ("a".upper())
  
# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
    # A total of 2 test cases
    with pytest.raises(ValueError, match=r"Score must be between 0 and 100."):
        convert_to_letter_grade(101)
        convert_to_letter_grade(-1.0)

# TODO-3: Add test_non_numeric_input() function
def test_non_numeric_input():
    # A total of 3 test cases
    with pytest.raises(TypeError, match=r"Score must be a numeric value."):
        convert_to_letter_grade("string")
        convert_to_letter_grade(["list"])
        convert_to_letter_grade(None)
