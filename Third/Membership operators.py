#Membership operators   = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                         1. in
#                         2. not in

# secret_word = "hippopotamus"

# letter = input("Guess a letter in a random word: \n" )
# letter = letter.lower()

# if letter in secret_word:
#     print(f"The letter {letter} is in the word!")
# else:
#     print(f"{letter} was not in the word.")

# students = ["Spongebob", "Patrick", "Sandy"]

# student = input("Guess the spongebob characters to see if they're students: \n")
# student = student.capitalize()

# if student in students:
#     print(f"Yes, {student} is a student.")
# else:
#     print(f"No, {student} is not a student.")

# grades = {"Sandy": "A",
#           "Squidward": "B",
#           "Spongebob": "C",
#           "Patrick": "D"}

# student = input("Enter a student's name: \n")
# student = student.capitalize()

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found!")

email = "plaokJorm@gmail.com"

if "@" and "." in email:
    print(f"{email} is a valid email.")
else:
    print(f"{email} is not a valid email.")
