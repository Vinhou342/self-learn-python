questions = (("How many elements are in the periodic table?"),
             ("Which any animal lays the largest egg?"),
             ("What is the most abundant gas in Earth's atmosphere?"), 
             ("How many bones are in the human body?"),
             ("Which plant in the solar system is the hottest?"))

options = (("A.116", "B.117", "C.118", "D.119"                        ),
           ("A.Whale", "B.Crocodile", "C.Elephant", "D.Ostrich"       ),
           ("A.Nitrogen", "B.Oxygen", "C.Carbon-dioxide", "D.Hydrogen"),
           ("A.206", "B.207", "C.208", "D.209"                        ),
           ("A.Mercury", "B.Venus", "C.Earth", "D.Mars"               ))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)

    while True:
        guess = input("Enter your guess (A, B, C, D): ").upper()
    
        if guess not in ["A", "B", "C", "D"]:
            print("Please choose a valid answer.")
            continue
        break           # exit loop when a valid input is given

    guesses.append(guess)

    if guess == answers[questions_num]:
        score += 1
        print("Correct!")
    else :
        print("Incorrect!")
        print(f"The correct answer is {answers[questions_num]}!")

    questions_num += 1

print("--------------------------")
print("         RESULTS          ")
print("--------------------------")

print("answers: ", end="\n")
for answer in answers:
    print(answer, end=" ")
print()

print("Your guesses: ", end = "\n")
for guess in guesses:
    print(guess, end= " ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")
