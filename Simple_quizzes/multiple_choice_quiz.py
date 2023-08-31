# multiple_choice_quiz TrybyFry
import time

play = input("Do you want to play a game? ")

if play.lower() != "yes":
    quit()
print("Lets have some fun!!!")


questions = ("What symbol is used for addition? ",
             "What symbol is used for subtraction? ",
             "What symbol is used for multiplication? ",
             "What symbol is used for division? ",
             "What symbol is used for equals? ",
             "What symbol is used for greater than? ",
             "What symbol is used for less than? ",
             "What symbol is used for greater than or equal to? ",
             "What symbol is used for less than or equal to? ")

options = (("A. +", "B. -", "C. *", "D. /"),
           ("A. =", "B. -", "C. <", "D. /"),
           ("A. +", "B. -", "C. *", "D. $"),
           ("A. -", "B. !", "C. #", "D. /"),
           ("A. +", "B. =", "C. >", "D. *"),
           ("A. >", "B. <", "C. +", "D. @"),
           ("A. +", "B. -", "C. >", "D. <"),
           ("A. +=", "B. -=", "C. <=", "D. >="),
           ("A. +=", "B. -=", "C. <=", "D. >="))

answers = ("A", "B", "C", "D", "B", "A", "D", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("<><><><><><><><><><><>")
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

print(">>>>>>>>>>>>>>>>>>>>>>")
print("       RESULTS        ")
print("<<<<<<<<<<<<<<<<<<<<<<")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
time.sleep(20)
