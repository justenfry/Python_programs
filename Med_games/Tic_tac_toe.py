#Tic tac toe TrybyFry
import time
import os 
game ={'7':' ','8':' ','9':' ',
       '4':' ','5':' ','6':' ',
       '1':' ','2':' ','3':' '}
def print_board(game):
    print(game['7'] + "|"+ game ['8']+ "|" + game['9'])
    print('-+-+-')
    print(game['4'] + "|"+ game['5'] + "|" + game['6'])
    print('-+-+-')
    print(game['1'] + "|"+ game['2'] + "|" + game['3'])
    
def win_check(game):
    #Horizontal wins
    if game['7'] == game['8'] == game['9'] != " ":
        print('Winner is ',game['8'])
        time.sleep(10)
        quit()
    elif game['4'] == game['5'] == game['6'] != " ":
        print('Winner is ',game['5'])
        time.sleep(10)
        quit()
    elif game['1'] == game['2'] == game['3'] != " ":
        print('Winner is ',game['2'])
        time.sleep(10)
        quit()
    #Vertical Wins
    elif game['7'] == game['4'] == game['1'] != " ":
        print('Winner is ',game['4'])
        time.sleep(10)
        quit()
    elif game['8'] == game['5'] == game['2'] != " ":
        print('Winner is ',game['5'])
        time.sleep(10)
        quit()
    elif game['9'] == game['6'] == game['3'] != " ":
        print('Winner is ',game['6'])
        time.sleep(10)
        quit()
    #Diagonal Win Condition
    elif game['1'] == game['5'] == game['9'] != " ":
        print('Winner is ',game['5'])
        time.sleep(10)
        quit()
    elif game['7'] == game['5'] == game['3'] != " ":
        print('Winner is ',game['5'])
        time.sleep(10)
        quit()
    """elif  game['1'] and game['5'] and game['3'] and game['4'] and game['8'] and game['6'] and game['7'] and game['2'] and game['9'] != " ":
        print('Stalemate, sorry try again ;)')
        time.sleep(10)
        quit()"""
i = 0 
print ("Welcome to Tic-Tac-Toe")
while True:
    print_board(game)
    turn = 'X'
    while i < 9:
        move = input('Choose your position: ')
        if game[move] == " ":
            game[move] = turn
            print_board(game)
            win_check(game)
            if turn == 'X':
                turn = 'O'
            elif turn =='O':
                turn = 'X'
            i += 1
        else:
            print('Choose another place')
    print('Stalemate, sorry try again ;)')
    replay = input('Do you want to play again?').lower()
    if replay == 'yes':
        while i >= 1:
            game[str(i)] = " "
            i -= 1
    elif replay == 'no':
        ('Thank you for playing')
        time.sleep(10)
        quit()
    os.system('cls')
