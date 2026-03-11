from data0 import *
from colors import regular_colors, reset, background
import random

# dictionary student names with numeric grades
grades = dict()

for name in student_names:
    grades[name] = random.randint(500, 1000)/100

print(grades)

# dictionary comprehension for grades




# dictionary with names and letter grades
letter_grades = list(grade_scale_13_steps.keys())

grades_letters = {}

for name in student_names:
    grades_letters[name] = random.choice(letter_grades)

# print(grades_letters)

# Grade with letters based on score function
def get_letter_grade(score):
    """
    Returns the letter grade based on the 13-step scale.
    If the score is below 5.00, it returns 'F'.
    """
    for letter, threshold in grade_scale_13_steps.items():
        if score >= threshold:
            return letter
    
    return "F"  # Fallback for scores below 5.00

# print on the terminal every element of the grades dictionary
# in a single line with grade and letter
# exemple:
# RESET = reset['Reset']
# RANDOM_COLOR = random.choices(list(regular_colors.values()))
# AG = grades["Alice"]
# print("Exemple:")
# print(f"{RANDOM_COLOR[0]}Alice got a {AG} score with a grade of {get_letter_grade(AG)}{RESET}")

