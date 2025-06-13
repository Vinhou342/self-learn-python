is_running = True
list = []

while is_running:
    
    task = input("Enter a chore to finish (q to quit): \n").lower()

    if task.isdigit():
        print("Enter a chore/work. Not numbers or symbols.")
        print("(q to quit).")
        print()
        continue

    elif not task.isdigit():
        list.append(task)
        
        if task == "q":
            list.remove("q")

            print(f"Number of task: {len(list)}")
            print(f"Total to-do list: {list}")

            sort = list.sort()
            print(f"Sorted list: {list}")

            reverse = list.reverse()
            print(f"Reversed list: {list}")

            pop = list.pop()
            print(f"Popped item: {pop}")
            
            if list == []:
                print("(after pop).")
                print("List = [].")
            else:
                print(f"Remaining after pop: {list}")

            if list == []:
                print("(after min and max.)")
                print("List = [].")
            else:
                print(f"Minimum: {min(list)}")
                print(f"Maximum: {max(list)}")
            
            break






    