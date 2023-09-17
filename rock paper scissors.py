from getpass import getpass as input
print('Welcome to 2 player Rock, Paper, Scissors game')
print('\033[34m','''Choose between Rock, Paper or Scissors.
    Enter
    R for Rock
    P for Paper
    S for Scissors
    ''','\033[0m')
player_1_score = 0
player_2_score = 0
while True:
    if player_1_score == 3:
        break
    if player_2_score ==3:
        break
    print('Current score is:','\n','Player 1 = ',player_1_score,'\n','Player 2 = ',player_2_score)
    player_1 = str(input('Player 1 > ')).capitalize()
    if player_1 not in ('S','R','P'):
        print('\033[31m','INVALID INPUT PLAYER 1','\033[0m')
        continue
    player_2 = str(input('Player 2 > ')).capitalize()
    if player_2 not in ('S','R','P'):
        print('\033[31m','INVALID INPUT PLAYER 2','\033[0m')
        continue
    if player_1 == 'R' and player_2 == 'P':
        print("Player 2 wins. Rock get's smothered by paper ")
        player_2_score += 1
    elif player_1 == 'P' and player_2 == 'R':
        print("Player 1 wins. Rock get's smothered by paper ")
        player_1_score +=1
    elif player_1 == 'R' and player_2 == 'S':
        print("Player 1 wins. Scissors get's hammered by rock ")
        player_1_score += 1
    elif player_1 == 'S' and player_2 == 'R':
        print("Player 2 wins. Scissors get's hammered by rock ")
        player_2_score +=1
    elif player_1 == 'P' and player_2 == 'S':
        print("Player 2 wins. Paper get's cut by a scissors ")
        player_2_score +=1
    elif player_1 == 'S' and player_2 == 'P':
        print("Player 1 wins. Paper get's cut by a scissors ")
        player_1_score +=1
    else:
        print("Well great minds think alike. It's a stalemate.")
        print('We are not adding this to the score.')
print()
if player_1_score > player_2_score :
    print('Player 1 won.')
    print(f'The score is {player_1_score} for player 1 and {player_2_score} for player 2')
    print('Game over')
elif player_1_score < player_2_score :
     print('Player 2 won.')
     print(f'The score is {player_2_score} for player 1 and {player_1_score} for player 2')
     print('Game over')
else:
    print('Game error')