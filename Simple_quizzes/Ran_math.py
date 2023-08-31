#Random math generator TrybyFry
import random
import time

choice = ('Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponent')
run = True
total = 0
score = 0
User_input = int(input("""Select math operation: 
1.Addition.
2.Subtraction. 
3.Multiplication. 
4.Division. 
5.Exponent.

Type 9999 to quit
Please enter your Choice(1-5)"""))
print("You chose", choice[User_input -1])
c = ('+', '-', '*', '/', '**')
range_2 = int(input('Enter highest value: '))
while run == True:
    Ra = random.randint(1, range_2)
    Rb = random.randint(1, range_2)
    if User_input == 1:
        print(Ra, c[0], Rb)
        answer = Ra + Rb
        user_answer = int(input())
        if user_answer == 9999:
            run = False
        elif user_answer == answer:
            print("Correct!")
            score += 1
            total += 1 

        else:
            print('Wrong! the correct answer is', answer)
            total += 1

    elif User_input == 2:
        print(Ra, c[1], Rb)
        answer = Ra - Rb
        user_answer = int(input())
        if user_answer == 9999:
            run = False
        elif user_answer == answer:
            print("Correct!")
            score += 1
            total += 1 
        else:
                print('Wrong! the correct answer is', answer)
                total += 1

    elif User_input == 3:
        print(Ra, c[2], Rb)
        answer = Ra * Rb
        user_answer = int(input())
        if user_answer == 9999:
            run = False
        elif user_answer == answer:
            print("Correct!")
            score += 1
            total += 1 
        else:
            print('Wrong! the correct answer is', answer)

    elif User_input == 4:
        print(Ra, c[3], Rb)
        answer = Ra / Rb
        user_answer = float(input())
        if user_answer == 9999:
            run = False
        elif user_answer == round(answer,2):
            print("Correct!")
            score += 1
            total += 1 
        else:
                print('Wrong! the correct answer is', round(answer,2))
                total += 1

    elif User_input == 5:
        print(Ra, 'to the power of 2')
        answer = Ra ** 2
        user_answer = int(input())
        if user_answer == 9999:
            run = False
        elif user_answer == round(answer,2):
            print("Correct!")
            score += 1
            total += 1
        else:
                print('Wrong! the correct answer is', answer)
                total += 1

    else:
        print("Your choice was out of range!!! Try again dinkus!")
print('You scored', score, 'out of ', total)
time.sleep(20)