"""
SCHOOL MANAGEMENT SYSTEM - STUDENT TEMPLATE
===========================================
Instructions: Fill in the missing code in the methods marked with TODO.
Follow the comments to complete each class.
"""

# ============================================
# STEP 1: STUDENT CLASS
# ============================================

class Student:
    """
    TODO: Create a class to represent a student.
    
    Instructions:
    1. Create the __init__ method with parameters: self, student_id, name, grade_level
    2. Store these as instance variables
    3. Create a display_info method that prints student details
    4. Create __str__ method for string representation
    """
    
    def __init__(self, student_id, name, grade_level):
        # TODO: Initialize the attributes
        # YOUR CODE HERE
        pass
    
    def display_info(self):
        # TODO: Print student information in a formatted way
        # Example: "ID: 1001 | Name: Alice | Grade: 10"
        # YOUR CODE HERE
        pass
    
    def __str__(self):
        # TODO: Return a string representation of the student
        # Example: "Student(ID: 1001, Name: Alice, Grade: 10)"
        # YOUR CODE HERE
        pass


# ============================================
# STEP 2: CLASS CLASS (School Course)
# ============================================

class Class:
    """
    TODO: Create a class to represent a school course.
    
    Instructions:
    1. Initialize with class_id, class_name, teacher
    2. Create an empty list for enrolled_students
    3. Create methods to add/remove students
    4. Create method to list all students in the class
    """
    
    def __init__(self, class_id, class_name, teacher):
        # TODO: Initialize attributes and an empty list for enrolled students
        # YOUR CODE HERE
        pass
    
    def add_student(self, student):
        # TODO: Add a student to the enrolled_students list
        # Check if student is already enrolled to avoid duplicates
        # Print success or warning message
        # YOUR CODE HERE
        pass
    
    def remove_student(self, student):
        # TODO: Remove a student from the enrolled_students list
        # Check if student exists before removing
        # Print appropriate messages
        # YOUR CODE HERE
        pass
    
    def list_students(self):
        # TODO: Display all students enrolled in this class
        # Handle case when no students are enrolled
        # YOUR CODE HERE
        pass
    
    def __str__(self):
        # TODO: Return string representation of the class
        # Include class ID, name, teacher, and number of students
        # YOUR CODE HERE
        pass


# ============================================
# STEP 3: GRADE CLASS
# ============================================

class Grade:
    """
    TODO: Create a class to represent a student's grade in a class.
    
    Instructions:
    1. Initialize with grade_id, student, class_obj, score
    2. Create a method to convert numerical score to letter grade
    3. Create a method to display grade information
    """
    
    def __init__(self, grade_id, student, class_obj, score):
        # TODO: Initialize all attributes
        # YOUR CODE HERE
        pass
    
    def get_letter_grade(self):
        """
        Convert numerical score to letter grade.
        Use this scale:
        90-100: A
        80-89: B
        70-79: C
        60-69: D
        Below 60: F
        """
        # TODO: Return the appropriate letter grade based on self.score
        # YOUR CODE HERE
        pass
    
    def display_grade(self):
        # TODO: Print grade information including letter grade
        # Example: "Grade ID: 301 | Student: Alice | Class: Math | Score: 95 | Letter: A"
        # YOUR CODE HERE
        pass
    
    def __str__(self):
        # TODO: Return string representation of the grade
        # Include letter grade in the string
        # YOUR CODE HERE
        pass


# ============================================
# STEP 4: SCHOOL MANAGEMENT SYSTEM
# ============================================

class School:
    """
    TODO: Create the main school management class.
    
    This class will manage all students, classes, and grades.
    """
    
    def __init__(self, school_name):
        # TODO: Initialize school name and empty lists for students, classes, and grades
        # YOUR CODE HERE
        pass
    
    # ---------- STUDENT MANAGEMENT ----------
    
    def add_student(self, student_id, name, grade_level):
        # TODO: Create a new Student object and add to students list
        # Check if student_id already exists
        # Return the new student or None if failed
        # YOUR CODE HERE
        pass
    
    def find_student(self, student_id):
        # TODO: Find and return a student by ID
        # Return None if not found
        # YOUR CODE HERE
        pass
    
    def list_all_students(self):
        # TODO: Display all students in the school
        # Handle empty list case
        # YOUR CODE HERE
        pass
    
    # ---------- CLASS MANAGEMENT ----------
    
    def add_class(self, class_id, class_name, teacher):
        # TODO: Create a new Class object and add to classes list
        # Check if class_id already exists
        # Return the new class or None if failed
        # YOUR CODE HERE
        pass
    
    def find_class(self, class_id):
        # TODO: Find and return a class by ID
        # Return None if not found
        # YOUR CODE HERE
        pass
    
    def list_all_classes(self):
        # TODO: Display all classes in the school
        # Include number of students enrolled in each class
        # YOUR CODE HERE
        pass
    
    # ---------- ENROLLMENT MANAGEMENT ----------
    
    def enroll_student_in_class(self, student_id, class_id):
        # TODO: Enroll a student in a class
        # Find both student and class first
        # Use the class's add_student method
        # Return True if successful, False otherwise
        # YOUR CODE HERE
        pass
    
    # ---------- GRADE MANAGEMENT ----------
    
    def add_grade(self, grade_id, student_id, class_id, score):
        # TODO: Add a grade for a student in a class
        # Verify student and class exist
        # Verify student is enrolled in the class
        # Check if grade_id already exists
        # Create and add new Grade object
        # YOUR CODE HERE
        pass
    
    def list_grades_for_student(self, student_id):
        # TODO: Display all grades for a specific student
        # YOUR CODE HERE
        pass
    
    def list_grades_for_class(self, class_id):
        # TODO: Display all grades for a specific class
        # YOUR CODE HERE
        pass
    
    def calculate_student_average(self, student_id):
        # TODO: Calculate and display average grade for a student
        # Return the average or None if no grades
        # YOUR CODE HERE
        pass


# ============================================
# STEP 5: MAIN PROGRAM WITH SAMPLE DATA
# ============================================

def main():
    """
    TODO: Create the main program with sample data and menu system.
    
    Instructions:
    1. Create a School object
    2. Add sample data (students, classes, enrollments, grades)
    3. Create an interactive menu system
    """
    
    print("=" * 60)
    print("🏫 WELCOME TO THE SCHOOL MANAGEMENT SYSTEM 🏫")
    print("=" * 60)
    
    # TODO: Create your school
    # school = School("Your School Name")
    
    # TODO: Add sample students
    # Use the data from the tutorial or create your own
    
    # TODO: Add sample classes
    
    # TODO: Enroll students in classes
    
    # TODO: Add sample grades
    
    # TODO: Create the interactive menu system
    # Include options to:
    # - List all students
    # - List all classes
    # - Add a new student
    # - Add a new class
    # - Enroll student in class
    # - Add a grade
    # - View student grades
    # - View class grades
    # - Calculate student average
    # - Exit
    
    # HINT: Use a while loop and if/elif statements for the menu
    
    # YOUR CODE HERE
    pass


# ============================================
# RUN THE PROGRAM
# ============================================

if __name__ == "__main__":
    main()


# ============================================
# BONUS CHALLENGES (Optional)
# ============================================

"""
Once you complete the basic system, try these challenges:

1. Add a Teacher class with attributes (teacher_id, name, subjects)
2. Add a method to calculate class average
3. Add search functionality (find students by name)
4. Add data persistence (save to and load from a file)
5. Add a report card generator
6. Add GPA calculation (4.0 scale)
7. Add attendance tracking
8. Add student schedules/timetables
"""

# ============================================
# ANSWER KEY (For teachers)
# ============================================

"""
The complete solution is available in the tutorial document.
Students should refer to the tutorial for guidance but try to
write the code themselves first.
"""

