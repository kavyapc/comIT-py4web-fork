```BASH
╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                              SCHOOL MANAGEMENT SYSTEM - CLASS DIAGRAM                                 ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────┐         ┌─────────────────────────────────┐
│            STUDENT              │         │             CLASS               │
├─────────────────────────────────┤         ├─────────────────────────────────┤
│ - student_id : int              │         │ - class_id : int                │
│ - name : str                    │         │ - class_name : str              │
│ - grade_level : int             │         │ - teacher : str                 │
├─────────────────────────────────┤         │ - enrolled_students : list      │
│ + __init__(id, name, grade)     │         ├─────────────────────────────────┤
│ + display_info() : void         │────────▶│ + __init__(id, name, teacher)   │
│ + __str__() : str               │         │ + add_student(student) : void   │
└─────────────────────────────────┘         │ + remove_student(student) : void│ls
                      ▲                     │ + list_students() : void        │
                      │                     │ + __str__() : str               │
                      │                     └─────────────────────────────────┘
                      │                                    ▲
                      │                                    │
                      │                                    │
┌─────────────────────────────────┐         ┌─────────────────────────────────┐
│             GRADE               │         │             SCHOOL              │
├─────────────────────────────────┤         ├─────────────────────────────────┤
│ - grade_id : int                │         │ - school_name : str             │
│ - student : Student             │         │ - students : list               │
│ - class_obj : Class             │         │ - classes : list                │
│ - score : float                 │         │ - grades : list                 │
├─────────────────────────────────┤         ├─────────────────────────────────┤
│ + __init__(id, student, class,  │         │ + __init__(name) : void         │
│            score)               │         │                                 │
│ + get_letter_grade() : str      │         │ + add_student(id, name, grade)  │
│ + display_grade() : void        │────────▶│ + find_student(id) : Student    │
│ + __str__() : str               │         │ + list_all_students() : void    │
└─────────────────────────────────┘         │ + add_class(id, name, teacher)  │
                                            │ + find_class(id) : Class        │
                                            │ + list_all_classes() : void     │
                                            │ + enroll_student(id, class)     │
                                            │ + add_grade(id, student, class, │
                                            │            score)               │
                                            │ + list_grades_for_student(id)   │
                                            │ + list_grades_for_class(id)     │
                                            │ + calculate_student_average(id) │
                                            └─────────────────────────────────┘

╔════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                     RELATIONSHIPS                                                      ║
╠════════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                        ║
║  [STUDENT] 1 ────────────────────────────── * [GRADE] : A student can have many grades                 ║
║                                                                                                        ║
║  [CLASS] 1 ──────────────────────────────── * [GRADE] : A class can have many grades                   ║
║                                                                                                        ║
║  [CLASS] 1 ──────────────────────────────── * [STUDENT] : A class has many students                    ║
║        (through enrolled_students list)                 (many-to-many relationship)                    ║
║                                                                                                        ║
║  [SCHOOL] 1 ─────────────────────────────── * [STUDENT] : A school manages many students               ║
║                                                                                                        ║
║  [SCHOOL] 1 ─────────────────────────────── * [CLASS] : A school offers many classes                   ║
║                                                                                                        ║
║  [SCHOOL] 1 ─────────────────────────────── * [GRADE] : A school tracks many grades                    ║
║                                                                                                        ║
╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                   METHOD DETAILS                                                      ║
╠═══════════════════════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                                       ║
║  STUDENT CLASS:                                                                                       ║
║  • __init__ : Constructor - initializes a new student                                                 ║
║  • display_info : Prints student details in formatted way                                             ║
║  • __str__ : Returns string representation of student                                                 ║
║                                                                                                       ║
║  CLASS CLASS:                                                                                         ║
║  • __init__ : Constructor - initializes a new class and empty student list                            ║
║  • add_student : Adds a student to the class (checks for duplicates)                                  ║
║  • remove_student : Removes a student from the class                                                  ║
║  • list_students : Displays all students in the class                                                 ║
║  • __str__ : Returns string representation of class                                                   ║
║                                                                                                       ║
║  GRADE CLASS:                                                                                         ║
║  • __init__ : Constructor - initializes a new grade                                                   ║
║  • get_letter_grade : Converts numerical score to letter grade (A, B, C, D, F)                        ║
║  • display_grade : Prints grade details with letter grade                                             ║
║  • __str__ : Returns string representation of grade                                                   ║
║                                                                                                       ║
║  SCHOOL CLASS:                                                                                        ║
║  • __init__ : Constructor - initializes school name and empty lists                                   ║
║  • add_student : Creates and adds a new student                                                       ║
║  • find_student : Searches for a student by ID                                                        ║
║  • list_all_students : Displays all students in school                                                ║
║  • add_class : Creates and adds a new class                                                           ║
║  • find_class : Searches for a class by ID                                                            ║
║  • list_all_classes : Displays all classes in school                                                  ║
║  • enroll_student_in_class : Enrolls a student in a class                                             ║
║  • add_grade : Creates and adds a new grade                                                           ║
║  • list_grades_for_student : Shows all grades for a specific student                                  ║
║  • list_grades_for_class : Shows all grades for a specific class                                      ║
║  • calculate_student_average : Calculates average grade for a student                                 ║
║                                                                                                       ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════╝
```