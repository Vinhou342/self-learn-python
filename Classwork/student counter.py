is_running = True

while is_running:
    print()
    print()

    num_stud = input("Enter the amount of students (whole positive integers): \n")
    if num_stud.isdigit():
        num_stud = int(num_stud)

        if num_stud < 0 or num_stud > 25:
            print("The amount of students can't be less than 0.")
            print("And cannot exceed 25.")
        else:
            print(f"Confirmed! The total amount of students is {num_stud}.")
            print("Thank you!")
            print()
            print()
            break           #OR "is_running = False"


