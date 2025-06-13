cat = {"Mab": "white", "Pich": "orange", "Dollar": "Platinum", "Kla": "Calico" }

while True:
    print("Enter a cat's name (blank to quit):")
    name = input().capitalize()

    if name == '':
        break
    if name in cat:
        print(f"{name} exist. It's fur is {cat.get(name)}")
    else: 
        print(f"I don't have info on {name}.")
        print("What is it's fur? \n")
        fur = input()
        cat[name] = fur
        print("Database updated.")

for key, value in cat.items():
    print(f"{key}: {value}.")