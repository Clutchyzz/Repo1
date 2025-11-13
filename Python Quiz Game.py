
questions = ("What is the most common animal in NYC?: ",
             "Whats the average Decible in NYC?: ",
             "What is a nested loop?: ",
             "Whats the tallest building in NYC?: ",
             "How many sisters do you have?: ")

options = (("A. Rat", "B. Dog", "C. Cat", "D, Bear"),
           ("A. 100db", "B. 20db", "C. 0db", "D, 90db"),
           ("A. A Loop", "B. A Collection", "C. A Variable", "D, A Loop inside a Loop"),
           ("A. Empire", "B. Summmit", "C. World Trade Center", "D, Chystler"),
           ("A. 1", "B. 2", "C. 3", "D, 4"))

answers = ("A", "A", "D", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is {score}%")