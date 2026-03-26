def validate_grades(grades):
    if len(grades) == 0:
        return False
    for grade in grades:
        if not isinstance(grade, int):
            return False
    return True

def add_student(students, name, age, grades, email):
    student_id = len(students)
    type_checks = [
        (name, str, "Student name must be a string"),
        (age, int, "Student age must be a number"),
        (grades, tuple, "Student grades must be a tuple"),
        (email, str, "Student email must be a string")
    ]

    for value, expected_type, error_message  in type_checks:
        if not isinstance(value, expected_type):
            print(error_message)
            return

    if not validate_grades(grades):
        print("There must be at least one grade, and all grades must be an integer")
        return

    if age < 0 or age > 100:
        print("The age must be between 0 and 100")
        return

    student_id += 1

    student_entry = {
        "id" : student_id,
        "name" : name,
        "age" : age,
        "grades" : grades,
        "email" : email
    }

    students.append(student_entry)

def classify_student(student):
    total_grades = 0
    if len(student["grades"]) == 0:
        print("The grades list is empty")
        return None

    for grade in student["grades"]:
        total_grades += grade

    average_grade = total_grades / len(student["grades"])

    if average_grade >= 90:
        return "Excellent"
    elif 70 <= average_grade < 90:
        return "Good"
    elif 50 <= average_grade < 70:
        return "Needs Improvement"
    else:
        return "At Risk"

def search_students(students, query):
    students_to_return = [ ]
    if not isinstance(query, str):
        print("The query must be a string")
        return None

    if len(query) == 0:
        print("The query must not be empty")
        return None

    lowercase_query = query.lower()

    for student in students:
        name_property = student["name"]
        lowercase_name = name_property.lower()
        name_length = len(name_property)
        query_length = len(query)
        for start_index in range((name_length + 1) - query_length):
            print(lowercase_name[start_index:query_length + start_index])
            if lowercase_name[start_index:query_length + start_index] == lowercase_query:
                students_to_return.append(student)
                break

    if len(students_to_return) == 0:
        return "No matches found"
    else:
        return students_to_return

def display_students(students, debug_mode=False):
    fields_to_display = { "id" : '', "name" : '', "age" : '', "grades" : '', "email" : '' }
    output = ''
    for student in students:
        for key in fields_to_display:
            data_type = str(type(student[key]))
            fields_to_display[key] = str(student[key])
            if debug_mode:
                fields_to_display[key] += ' ' + data_type

        output +=  f'ID: {fields_to_display['id']}\nName: {fields_to_display['name']}\nAge: {fields_to_display['age']}\nGrades: {fields_to_display['grades']}\nE-mail: {fields_to_display['email']}\n\n'

    return output

def should_contact_parent(student):
    if classify_student(student) == 'At Risk' and len(student["email"]) > 0:
        return True
    elif classify_student(student) == 'Needs Improvement' and student["age"] < 16:
        return True
    else:
        return False


