# Tuple containing student records (ID, Name, Age, Grade)
students = (
    (101, "Alice", 20, "A"),
    (102, "Bob", 21, "B"),
    (103, "Charlie", 22, "A"),
    (104, "David", 20, "C"),
)

# Function to search for a student by ID
def find_student(student_id):
    for student in students:
        if student[0] == student_id:
            return student
    return "Student not found"

# Test the function
search_id = int(input("Enter student ID to search: " + "\n"))
print(find_student(search_id))