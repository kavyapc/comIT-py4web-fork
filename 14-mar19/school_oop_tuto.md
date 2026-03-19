# School Management System - Python OOP Tutorial

## Table of Contents
- [School Management System - Python OOP Tutorial](#school-management-system---python-oop-tutorial)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Project Structure](#project-structure)
  - [Step 1: Creating the Student Class](#step-1-creating-the-student-class)
  - [Step 2: Creating the Class Class](#step-2-creating-the-class-class)
  - [Step 3: Creating the Grade Class](#step-3-creating-the-grade-class)
  - [Step 4: Creating the School Management System](#step-4-creating-the-school-management-system)
  - [Step 5: Creating the Main Program](#step-5-creating-the-main-program)
  - [Complete Code](#complete-code)
  - [Sample Data](#sample-data)
    - [Students](#students)
    - [Classes](#classes)
    - [Enrollments \& Grades](#enrollments--grades)
  - [How to Run the Program](#how-to-run-the-program)
  - [Practice Exercises](#practice-exercises)
  - [Key OOP Concepts Learned](#key-oop-concepts-learned)

## Introduction

Welcome! In this tutorial, you'll learn Object-Oriented Programming (OOP) by building a School Management System. This program will run in the terminal and help you understand:

- **Classes and Objects** - The building blocks of OOP
- **Attributes** - Data stored in objects
- **Methods** - Functions that belong to objects
- **Encapsulation** - Keeping related data and functions together

## Project Structure

Our School Management System will have four main classes:
```
├── Student      - Represents a student
├── Class        - Represents a school class/course
├── Grade        - Represents a student's grade in a class
└── School       - Manages everything (students, classes, grades)
```

## Step 1: Creating the Student Class

Let's start by creating a class to represent a student. Each student will have a unique ID, name, and grade level.

```python
class Student:
    """
    A class to represent a student.
    
    Attributes:
    -----------
    student_id : int
        Unique identifier for the student
    name : str
        Student's full name
    grade_level : int
        Student's grade level (9-12 for high school)
    """
    
    def __init__(self, student_id, name, grade_level):
        """
        Constructor method - runs when we create a new Student object.
        
        Parameters:
        -----------
        student_id : int
            Unique ID for the student
        name : str
            Student's name
        grade_level : int
            Student's grade level
        """
        self.student_id = student_id      # self refers to the instance being created
        self.name = name                  # Store the name in the object
        self.grade_level = grade_level    # Store the grade level
    
    def display_info(self):
        """
        Display student information in a formatted way.
        """
        print(f"ID: {self.student_id} | Name: {self.name} | Grade: {self.grade_level}")
    
    def __str__(self):
        """
        Special method that returns a string representation of the object.
        This is called when we print the object.
        """
        return f"Student(ID: {self.student_id}, Name: {self.name}, Grade: {self.grade_level})"
```

**Explanation:**
- `__init__` is the constructor - it initializes new objects
- `self` refers to the current instance of the class
- Attributes like `student_id` are stored in `self`
- Methods like `display_info()` define what the object can do

## Step 2: Creating the Class Class

Now let's create a class to represent a school class/course (like Math 101).

```python
class Class:
    """
    A class to represent a school class/course.
    
    Attributes:
    -----------
    class_id : int
        Unique identifier for the class
    class_name : str
        Name of the class (e.g., "Mathematics")
    teacher : str
        Name of the teacher
    """
    
    def __init__(self, class_id, class_name, teacher):
        """
        Initialize a new Class object.
        """
        self.class_id = class_id
        self.class_name = class_name
        self.teacher = teacher
        # List to store enrolled students (will be filled later)
        self.enrolled_students = []
    
    def add_student(self, student):
        """
        Add a student to this class.
        
        Parameters:
        -----------
        student : Student object
            The student to enroll
        """
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            print(f"✅ {student.name} added to {self.class_name}")
        else:
            print(f"⚠️ {student.name} is already enrolled in {self.class_name}")
    
    def remove_student(self, student):
        """
        Remove a student from this class.
        """
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(f"✅ {student.name} removed from {self.class_name}")
        else:
            print(f"⚠️ {student.name} is not enrolled in {self.class_name}")
    
    def list_students(self):
        """
        Display all students enrolled in this class.
        """
        print(f"\n📚 Students in {self.class_name} (Teacher: {self.teacher}):")
        if not self.enrolled_students:
            print("   No students enrolled yet.")
        else:
            for student in self.enrolled_students:
                print(f"   • {student.name} (ID: {student.student_id})")
    
    def __str__(self):
        return f"Class(ID: {self.class_id}, Name: {self.class_name}, Teacher: {self.teacher}, Students: {len(self.enrolled_students)})"
```

**Explanation:**
- This class has a list `enrolled_students` to keep track of who's in the class
- Methods like `add_student()` and `remove_student()` manage enrollment
- We check if a student is already enrolled to avoid duplicates

## Step 3: Creating the Grade Class

Now we need a way to track grades for students in classes.

```python
class Grade:
    """
    A class to represent a grade for a student in a class.
    
    Attributes:
    -----------
    grade_id : int
        Unique identifier for the grade record
    student : Student
        The student who received the grade
    class_obj : Class
        The class the grade is for
    score : float
        The grade score (0-100)
    """
    
    def __init__(self, grade_id, student, class_obj, score):
        """
        Initialize a new Grade object.
        """
        self.grade_id = grade_id
        self.student = student
        self.class_obj = class_obj
        self.score = score
    
    def get_letter_grade(self):
        """
        Convert numerical score to letter grade.
        """
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"
    
    def display_grade(self):
        """
        Display grade information in a formatted way.
        """
        letter = self.get_letter_grade()
        print(f"Grade ID: {self.grade_id} | Student: {self.student.name} | "
              f"Class: {self.class_obj.class_name} | Score: {self.score} | Letter: {letter}")
    
    def __str__(self):
        letter = self.get_letter_grade()
        return f"Grade(ID: {self.grade_id}, Student: {self.student.name}, Class: {self.class_obj.class_name}, Score: {self.score}, Letter: {letter})"
```

**Explanation:**
- This class connects a student with a class and a score
- The `get_letter_grade()` method shows how objects can have behavior
- We store the actual Student and Class objects, not just IDs

## Step 4: Creating the School Management System

This is the main class that will manage everything.

```python
class School:
    """
    Main school management system that coordinates students, classes, and grades.
    
    Attributes:
    -----------
    students : list
        List of all Student objects
    classes : list
        List of all Class objects
    grades : list
        List of all Grade objects
    """
    
    def __init__(self, school_name):
        """
        Initialize a new school with empty lists.
        """
        self.school_name = school_name
        self.students = []      # Will hold all Student objects
        self.classes = []       # Will hold all Class objects
        self.grades = []        # Will hold all Grade objects
    
    # ========== STUDENT MANAGEMENT ==========
    
    def add_student(self, student_id, name, grade_level):
        """
        Create and add a new student to the school.
        """
        # Check if student ID already exists
        for student in self.students:
            if student.student_id == student_id:
                print(f"❌ Student with ID {student_id} already exists!")
                return None
        
        # Create new student and add to list
        new_student = Student(student_id, name, grade_level)
        self.students.append(new_student)
        print(f"✅ Student {name} added successfully!")
        return new_student
    
    def find_student(self, student_id):
        """
        Find a student by their ID.
        Returns the Student object if found, None otherwise.
        """
        for student in self.students:
            if student.student_id == student_id:
                return student
        print(f"❌ Student with ID {student_id} not found!")
        return None
    
    def list_all_students(self):
        """
        Display all students in the school.
        """
        print(f"\n🎓 Students at {self.school_name}:")
        print("-" * 50)
        if not self.students:
            print("No students enrolled yet.")
        else:
            for student in self.students:
                student.display_info()
        print("-" * 50)
    
    # ========== CLASS MANAGEMENT ==========
    
    def add_class(self, class_id, class_name, teacher):
        """
        Create and add a new class to the school.
        """
        # Check if class ID already exists
        for class_obj in self.classes:
            if class_obj.class_id == class_id:
                print(f"❌ Class with ID {class_id} already exists!")
                return None
        
        # Create new class and add to list
        new_class = Class(class_id, class_name, teacher)
        self.classes.append(new_class)
        print(f"✅ Class {class_name} added successfully!")
        return new_class
    
    def find_class(self, class_id):
        """
        Find a class by its ID.
        """
        for class_obj in self.classes:
            if class_obj.class_id == class_id:
                return class_obj
        print(f"❌ Class with ID {class_id} not found!")
        return None
    
    def list_all_classes(self):
        """
        Display all classes in the school.
        """
        print(f"\n📚 Classes at {self.school_name}:")
        print("-" * 50)
        if not self.classes:
            print("No classes available yet.")
        else:
            for class_obj in self.classes:
                print(f"ID: {class_obj.class_id} | {class_obj.class_name} | Teacher: {class_obj.teacher} | Students: {len(class_obj.enrolled_students)}")
        print("-" * 50)
    
    # ========== ENROLLMENT MANAGEMENT ==========
    
    def enroll_student_in_class(self, student_id, class_id):
        """
        Enroll a student in a class.
        """
        student = self.find_student(student_id)
        if not student:
            return False
        
        class_obj = self.find_class(class_id)
        if not class_obj:
            return False
        
        # Add student to class
        class_obj.add_student(student)
        return True
    
    # ========== GRADE MANAGEMENT ==========
    
    def add_grade(self, grade_id, student_id, class_id, score):
        """
        Add a grade for a student in a class.
        """
        student = self.find_student(student_id)
        if not student:
            return None
        
        class_obj = self.find_class(class_id)
        if not class_obj:
            return None
        
        # Check if student is enrolled in the class
        if student not in class_obj.enrolled_students:
            print(f"❌ {student.name} is not enrolled in {class_obj.class_name}!")
            return None
        
        # Check if grade ID already exists
        for grade in self.grades:
            if grade.grade_id == grade_id:
                print(f"❌ Grade with ID {grade_id} already exists!")
                return None
        
        # Create and add grade
        new_grade = Grade(grade_id, student, class_obj, score)
        self.grades.append(new_grade)
        print(f"✅ Grade added for {student.name} in {class_obj.class_name}: {score}")
        return new_grade
    
    def list_grades_for_student(self, student_id):
        """
        Show all grades for a specific student.
        """
        student = self.find_student(student_id)
        if not student:
            return
        
        print(f"\n📊 Grades for {student.name}:")
        print("-" * 50)
        student_grades = [g for g in self.grades if g.student.student_id == student_id]
        
        if not student_grades:
            print("No grades recorded yet.")
        else:
            for grade in student_grades:
                grade.display_grade()
        print("-" * 50)
    
    def list_grades_for_class(self, class_id):
        """
        Show all grades for a specific class.
        """
        class_obj = self.find_class(class_id)
        if not class_obj:
            return
        
        print(f"\n📊 Grades for {class_obj.class_name}:")
        print("-" * 50)
        class_grades = [g for g in self.grades if g.class_obj.class_id == class_id]
        
        if not class_grades:
            print("No grades recorded yet.")
        else:
            for grade in class_grades:
                grade.display_grade()
        print("-" * 50)
    
    def calculate_student_average(self, student_id):
        """
        Calculate average grade for a student.
        """
        student = self.find_student(student_id)
        if not student:
            return None
        
        student_grades = [g for g in self.grades if g.student.student_id == student_id]
        
        if not student_grades:
            print(f"{student.name} has no grades yet.")
            return None
        
        total = sum(grade.score for grade in student_grades)
        average = total / len(student_grades)
        print(f"📈 {student.name}'s average grade: {average:.2f}")
        return average
```

## Step 5: Creating the Main Program

Now let's create a simple menu system to interact with our school.

```python
def main():
    """
    Main function to run the School Management System.
    """
    # Create our school
    school = School("Python High School")
    
    # ===== ADD SAMPLE DATA =====
    print("=" * 60)
    print("🏫 WELCOME TO THE SCHOOL MANAGEMENT SYSTEM 🏫")
    print("=" * 60)
    
    # Add some students
    print("\n📝 Adding sample students...")
    school.add_student(1001, "Alice Johnson", 10)
    school.add_student(1002, "Bob Smith", 11)
    school.add_student(1003, "Charlie Brown", 9)
    school.add_student(1004, "Diana Prince", 12)
    school.add_student(1005, "Evan Wright", 10)
    
    # Add some classes
    print("\n📝 Adding sample classes...")
    school.add_class(201, "Mathematics", "Dr. Smith")
    school.add_class(202, "Science", "Ms. Davis")
    school.add_class(203, "English Literature", "Mr. Johnson")
    school.add_class(204, "History", "Mrs. Williams")
    
    # Enroll students in classes
    print("\n📝 Enrolling students in classes...")
    school.enroll_student_in_class(1001, 201)  # Alice in Math
    school.enroll_student_in_class(1001, 202)  # Alice in Science
    school.enroll_student_in_class(1002, 201)  # Bob in Math
    school.enroll_student_in_class(1002, 203)  # Bob in English
    school.enroll_student_in_class(1003, 201)  # Charlie in Math
    school.enroll_student_in_class(1003, 204)  # Charlie in History
    school.enroll_student_in_class(1004, 202)  # Diana in Science
    school.enroll_student_in_class(1004, 203)  # Diana in English
    school.enroll_student_in_class(1005, 201)  # Evan in Math
    school.enroll_student_in_class(1005, 204)  # Evan in History
    
    # Add some grades
    print("\n📝 Adding sample grades...")
    school.add_grade(301, 1001, 201, 95)   # Alice - Math
    school.add_grade(302, 1001, 202, 88)   # Alice - Science
    school.add_grade(303, 1002, 201, 78)   # Bob - Math
    school.add_grade(304, 1002, 203, 92)   # Bob - English
    school.add_grade(305, 1003, 201, 85)   # Charlie - Math
    school.add_grade(306, 1003, 204, 90)   # Charlie - History
    school.add_grade(307, 1004, 202, 96)   # Diana - Science
    school.add_grade(308, 1004, 203, 89)   # Diana - English
    school.add_grade(309, 1005, 201, 82)   # Evan - Math
    school.add_grade(310, 1005, 204, 75)   # Evan - History
    
    # Display information
    print("\n" + "=" * 60)
    print("✅ SETUP COMPLETE! Here's the current status:")
    print("=" * 60)
    
    school.list_all_students()
    school.list_all_classes()
    
    # Show some example queries
    print("\n📊 Example: Alice's Grades")
    school.list_grades_for_student(1001)
    
    print("\n📊 Example: Math Class Grades")
    school.list_grades_for_class(201)
    
    print("\n📊 Example: Student Averages")
    school.calculate_student_average(1001)
    school.calculate_student_average(1002)
    
    # ===== INTERACTIVE MENU =====
    while True:
        print("\n" + "=" * 60)
        print("🏫 MAIN MENU")
        print("=" * 60)
        print("1. List all students")
        print("2. List all classes")
        print("3. Add a new student")
        print("4. Add a new class")
        print("5. Enroll student in class")
        print("6. Add a grade")
        print("7. View student grades")
        print("8. View class grades")
        print("9. Calculate student average")
        print("0. Exit")
        print("-" * 60)
        
        choice = input("Enter your choice (0-9): ")
        
        if choice == "1":
            school.list_all_students()
        
        elif choice == "2":
            school.list_all_classes()
        
        elif choice == "3":
            print("\n➕ Add New Student")
            try:
                student_id = int(input("Enter student ID: "))
                name = input("Enter student name: ")
                grade_level = int(input("Enter grade level (9-12): "))
                school.add_student(student_id, name, grade_level)
            except ValueError:
                print("❌ Invalid input! Please enter numbers for ID and grade level.")
        
        elif choice == "4":
            print("\n➕ Add New Class")
            try:
                class_id = int(input("Enter class ID: "))
                class_name = input("Enter class name: ")
                teacher = input("Enter teacher name: ")
                school.add_class(class_id, class_name, teacher)
            except ValueError:
                print("❌ Invalid input! Please enter a number for class ID.")
        
        elif choice == "5":
            print("\n📝 Enroll Student")
            try:
                student_id = int(input("Enter student ID: "))
                class_id = int(input("Enter class ID: "))
                school.enroll_student_in_class(student_id, class_id)
            except ValueError:
                print("❌ Invalid input! Please enter numbers for IDs.")
        
        elif choice == "6":
            print("\n📝 Add Grade")
            try:
                grade_id = int(input("Enter grade ID: "))
                student_id = int(input("Enter student ID: "))
                class_id = int(input("Enter class ID: "))
                score = float(input("Enter score (0-100): "))
                if 0 <= score <= 100:
                    school.add_grade(grade_id, student_id, class_id, score)
                else:
                    print("❌ Score must be between 0 and 100!")
            except ValueError:
                print("❌ Invalid input! Please check your entries.")
        
        elif choice == "7":
            print("\n📊 View Student Grades")
            try:
                student_id = int(input("Enter student ID: "))
                school.list_grades_for_student(student_id)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        elif choice == "8":
            print("\n📊 View Class Grades")
            try:
                class_id = int(input("Enter class ID: "))
                school.list_grades_for_class(class_id)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        elif choice == "9":
            print("\n📈 Calculate Student Average")
            try:
                student_id = int(input("Enter student ID: "))
                school.calculate_student_average(student_id)
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
        
        elif choice == "0":
            print("\n👋 Thank you for using the School Management System. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

# This is the standard way to run the main function
if __name__ == "__main__":
    main()
```

## Complete Code

You can copy all the code above into a single file called `school_management.py`. The code is organized in this order:

1. `Student` class
2. `Class` class
3. `Grade` class
4. `School` class
5. `main()` function
6. The `if __name__ == "__main__":` block

## Sample Data

Here's a summary of the sample data included:

### Students
| ID | Name | Grade Level |
|-----|------|-------------|
| 1001 | Alice Johnson | 10 |
| 1002 | Bob Smith | 11 |
| 1003 | Charlie Brown | 9 |
| 1004 | Diana Prince | 12 |
| 1005 | Evan Wright | 10 |

### Classes
| ID | Name | Teacher |
|-----|------|---------|
| 201 | Mathematics | Dr. Smith |
| 202 | Science | Ms. Davis |
| 203 | English Literature | Mr. Johnson |
| 204 | History | Mrs. Williams |

### Enrollments & Grades
| Student | Classes | Grades |
|---------|---------|--------|
| Alice (1001) | Math (95), Science (88) | A, B+ |
| Bob (1002) | Math (78), English (92) | C+, A- |
| Charlie (1003) | Math (85), History (90) | B, A- |
| Diana (1004) | Science (96), English (89) | A, B+ |
| Evan (1005) | Math (82), History (75) | B-, C |

## How to Run the Program

1. **Save the file** as `school_management.py`

2. **Open terminal/command prompt** and navigate to the folder where you saved the file

3. **Run the program:**
   ```bash
   python school_management.py
   ```

4. **Interact with the menu** using number keys (0-9)

## Practice Exercises

Once you understand the code, try these exercises:

1. **Add a new feature**: Create a method to calculate class average
2. **Improve validation**: Add checks for duplicate enrollments
3. **Add search functionality**: Find students by name
4. **Save/Load data**: Add functions to save to and load from a file
5. **Add more attributes**: Add student email, phone number, etc.
6. **Create reports**: Generate report cards for students

## Key OOP Concepts Learned

- **Classes** are blueprints for creating objects
- **Objects** are instances of classes
- **Attributes** store data in objects
- **Methods** define what objects can do
- **`self`** refers to the current instance
- **`__init__`** is the constructor method
- **Encapsulation** keeps related data and functions together

Happy coding! 🚀