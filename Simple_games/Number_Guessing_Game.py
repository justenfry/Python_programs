#Number_Guessing_Game TrybyFry
import time
import random
count = 1
answer = random.randrange(1,100)
print('Choose a number between 1 and 100')
mode = input('Choose your mode easy(unlimited) or hard mode(5 guess max)').lower()
if mode == 'easy':
    guess = input('Enter your number: ')
    while guess != answer :
        if int(guess) < int(answer):
            print ("Your guessed too low")
            guess=input('Guess again:')
            count += 1
        elif int(guess) > int(answer):
            print ("Your guessed too high")
            guess=input('Guess again:')
            count += 1
        else:
            break
    print('Congratulations you guess it in', count, 'guesses')
    time.sleep(10)
elif mode == 'hard':
    guess = input('Enter your number: ')
    while guess != answer:
        while count < 5:
            if int(guess) < int(answer):
                print ("Your guessed too low you have {} guesses remaining".format((5-count)))
                guess=input('Guess again:')
                count += 1
            elif int(guess) > int(answer):
                print ("Your guessed too high you have {} guesses remaining".format((5-count)))
                guess=input('Guess again:')
                count += 1
            elif int(guess) == int(answer):
                print('Congratulations you guess it in', count, 'guesses')
                time.sleep(10)
                quit()
        break
    print('Sorry you ran out of guesses the number was', answer)
    time.sleep(10)

elif mode != 'easy' or 'hard':
    print("OK jerk mode it is!!! You have one shot.")
    guess = input('Enter your number: ')
    if int(guess) == int(answer):
        print('You are a god!!!!')
        time.sleep(10)
    else:
        print('HAHAHA you suck monkey butt!!! It was ', answer)
        time.sleep(10)
