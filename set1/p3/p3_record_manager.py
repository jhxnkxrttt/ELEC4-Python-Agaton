# Agaton, Jhon Kurt V. IV-BSIT B
# P3: Student Record Manager
# November 23, 2026

students = []
student_set = set()

# Function 1: Add a student
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty!")
        return

    name_key = name.lower()

    if name_key in student_set:
        print("Student already exists!")
    else:
        students.append(name.title())
        student_set.add(name_key)
        print("Student added successfully!")

# Function 2: Remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()
    name_key = name.lower()

    if name_key in student_set:
        student_set.remove(name_key)

        for student in students:
            if student.lower() == name_key:
                students.remove(student)
                break

        print("Student removed successfully!")
    else:
        print("Student not found!")

# Function 3: Search for a student
def search_student():
    name = input("Enter name to search: ").strip().lower()

    matches = []

    for student in students:
        if name in student.lower():
            matches.append(student)

    if matches:
        print("\n SEARCH RESULTS ")
        for student in matches:
            print(student)
    else:
        print("Student not found!")

# Function 4: Display all students
def display_students():
    if len(students) == 0:
        print("No students in the record.")
        return

    sorted_students = sorted(students, key=str.lower)

    print("\n STUDENT LIST ")

    for index, student in enumerate(sorted_students, start=1):
        print(f"{index}. {student}")

    print("Total students:", len(students))


# A list stores student names and allows us to arrange and display them alphabetically.
# A set stores unique names and helps prevent duplicate student records.
# In my program, I used the list to display, search, and remove students.
# I used the set to check whether a student name already exists before adding it.