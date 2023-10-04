import random, os, time
print('Snake and Ladders')

#to chear the screen
def clear_screen():
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.system('clear')  # Clear the screen on other systems


#possible ladders
def ladder_1():
    time.sleep(1)
    print('You have found a ladder.')
    print("This ladder takes you from box 7 to box 25 ✨")
    time.sleep(3)
     
def ladder_2():
    time.sleep(1)
    print("You have found a ladder!")
    print("This ladder takes you from box 11 to box 87 ✨✨✨✨✨✨")
    time.sleep(3)

def ladder_3():
    time.sleep(1)
    print("You have found a ladder!")
    print("This ladder takes you from box 3 to box 35 ✨")
    time.sleep(3)

def ladder_4():
    time.sleep(1)
    print("You have found a ladder!")
    print("This ladder takes you from box 16 to box 58 ✨")
    time.sleep(3)

def ladder_5():
    time.sleep(1)
    print("You have found a ladder!")
    print("This ladder takes you from box 49 to box 70 ✨")
    time.sleep(3)


#possible snakes
def snake_1():
    time.sleep(1)
    print('Unfortunately you have landed on a box with a snake🐍')
    print("This snake takes you from box 97 to box 2😭😭😭😭😭😭😭")
    time.sleep(3)

def snake_2():
    time.sleep(1)
    print('Unfortunately you have landed on a box with a snake🐍')
    print("This snake takes you from box 81 to box 50😭")
    time.sleep(3)

def snake_3():
    time.sleep(1)
    print('Unfortunately you have landed on a box with a snake🐍')
    print("This snake takes you from box 20 to box 12😭")
    time.sleep(3)

def snake_4():
    time.sleep(1)
    print('Unfortunately you have landed on a box with a snake🐍')
    print("This snake takes you from box 77 to box 40😭")
    time.sleep(3)

def snake_5():
    time.sleep(1)
    print('Unfortunately you have landed on a box with a snake🐍')
    print("This snake takes you from box 44 to box 21😭")
    time.sleep(3)

def snake_6():
    time.sleep(1)
    print('Unfortunately you have landed on a box with a snake🐍')
    print("This snake takes you from box 30 to box 10😭")
    time.sleep(3)

#dice rolling function to cater for rolling a six and rolling again
def super_roll(rolled):
    total_rolled = rolled
    if rolled == 6:
        while True:
            print("WOW 🤩🤩😎😎! \n🤯You rolled a 6🤯 \n😉You get to roll again😉")
            roll = input('Press "r" to roll the dice: ')
            if roll == 'r':
                rolled = random.randint(1,6)
                total_rolled += rolled
                if rolled < 6:
                    print(f"You rolled {rolled}")
                    break
            else:
                print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
    return total_rolled            

def super_roll_computer(rolled):
    total_rolled = rolled
    if rolled == 6:
        while True:
            print("WOW 🤩🤩😎😎! \n🤯You rolled a 6🤯 \n😉You get to roll again😉")
            print('Press "r" to roll the dice: ', end = '')
            time.sleep(1)
            print('r')
            roll = 'r'
            if roll == 'r':
                rolled = random.randint(1,6)
                total_rolled += rolled
                if rolled < 6:
                    print(f"You rolled {rolled}")
                    break
            else:
                print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
    return total_rolled            

def movement_of_player_1(player_1_box,rolled):
    if (player_1_box + rolled) > 100 :
        movement = (player_1_box + rolled) - 100
        player_1_box =100 - movement

    if(player_1_box + rolled) <= 100 :
        player_1_box += rolled
    return player_1_box

def movement_of_player_2(player_2_box,rolled):
    if (player_2_box + rolled) > 100 :
        movement = (player_2_box + rolled) - 100
        player_2_box =100 - movement

    if(player_2_box + rolled) <= 100 :
        player_2_box += rolled
    return player_2_box

def movement_of_player_3(player_3_box,rolled):
    if (player_3_box + rolled) > 100 :
        movement = (player_3_box + rolled) - 100
        player_3_box =100 - movement

    if(player_3_box + rolled) <= 100 :
        player_3_box += rolled
    return player_3_box

def player_2_start_computer(player_2_box, starter2):
    start2 = False
    if starter2 == 6:
        start2 = True
    while not start2:
        print(f'You are in box number {player_2_box}.')
        print('Press "r" to roll the dice: ', end= '')
        time.sleep(1)
        print('r')
        roll = 'r'
        if roll == 'r':
            rolled = random.randint(1,6)
            print(f'You rolled {rolled}')
            if rolled == 6:
                player_2_box += 1
                print(f'Welcome you are in box {player_2_box}')
                starter2 = 6
                start2 = True
                break
            else:
                print("You didn't roll a six, try again!")
                break
        else:
            print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
            continue
    return player_2_box, start2, starter2

def player_2_game_computer(player_2_box):
    while True:
        print('Press "r" to roll the dice: ', end= '')
        time.sleep(1)
        print('r')
        roll = 'r'
        if roll == 'r':
            rolled = random.randint(1,6)

            total_rolled = super_roll_computer(rolled)
            rolled = total_rolled
            time.sleep(1)
            print(f"You rolled {rolled}")

            player_2_box = movement_of_player_1(player_2_box,rolled)
            time.sleep(1)
            print(f"You are now in box {player_2_box}")

            #possible ladders to climb
            if player_2_box ==  7:
                ladder_1()
                player_2_box = 25

            elif player_2_box ==  11:
                ladder_2()
                player_2_box = 87

            elif player_2_box ==  3:
                ladder_3()
                player_2_box= 35

            elif player_2_box ==  16:
                ladder_4()
                player_2_box = 58

            elif player_2_box ==  49:
                ladder_5()
                player_2_box = 70


            #possible snakes
            if player_2_box == 97:
                snake_1()
                player_2_box = 2

            elif player_2_box == 81:
                snake_2()
                player_2_box = 50

            elif player_2_box == 20:
                snake_3()
                player_2_box = 12

            elif player_2_box == 77:
                snake_4()
                player_2_box = 40

            elif player_2_box == 44:
                snake_5()
                player_2_box = 21

            elif player_2_box == 30:
                snake_6()
                player_2_box = 10
            break
                            
                            
        else:
            print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
            continue
    return player_2_box


def player_1_start(player_1_box, starter1):
    start1 = False
    if starter1 == 6:
        start1 = True
    while not start1:
        print(f'You are in box number {player_1_box}.')
        roll = input('Press "r" to roll the dice: ')
        if roll == 'r':
            rolled = random.randint(1,6)
            print(f'You rolled {rolled}')
            if rolled == 6:
                player_1_box += 1
                print(f'Welcome you are in box {player_1_box}')
                starter1 = 6
                start1 = True
                break
            else:
                print("You didn't roll a six, try again!")
                break
        else:
            print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
            continue
    return player_1_box, start1, starter1

def player_1_game(player_1_box):
    while True:
        roll = input('Press "r" to roll the dice: ')
        if roll == 'r':
            rolled = random.randint(1,6)

            total_rolled = super_roll(rolled)
            rolled = total_rolled
            time.sleep(1)
            print(f"You rolled {rolled}")

            player_1_box = movement_of_player_1(player_1_box,rolled)
            time.sleep(1)
            print(f"You are now in box {player_1_box}")

            #possible ladders to climb
            if player_1_box ==  7:
                ladder_1()
                player_1_box = 25

            elif player_1_box ==  11:
                ladder_2()
                player_1_box = 87

            elif player_1_box ==  3:
                ladder_3()
                player_1_box= 35

            elif player_1_box ==  16:
                ladder_4()
                player_1_box = 58

            elif player_1_box ==  49:
                ladder_5()
                player_1_box = 70


            #possible snakes
            if player_1_box == 97:
                snake_1()
                player_1_box = 2

            elif player_1_box == 81:
                snake_2()
                player_1_box = 50

            elif player_1_box == 20:
                snake_3()
                player_1_box = 12

            elif player_1_box == 77:
                snake_4()
                player_1_box = 40

            elif player_1_box == 44:
                snake_5()
                player_1_box = 21

            elif player_1_box == 30:
                snake_6()
                player_1_box = 10
            break
                            
                            
        else:
            print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
            continue
    return player_1_box

def player_2_start(player_2_box, starter2):
    start2 = False
    if starter2 == 6:
        start2 = True
    while not start2:
        print(f'You are in box number {player_2_box}.')
        roll = input('Press "r" to roll the dice: ')
        if roll == 'r':
            rolled = random.randint(1,6)
            print(f'You rolled {rolled}')
            if rolled == 6:
                player_2_box += 1
                print(f'Welcome you are in box {player_2_box}')
                starter2 = 6
                start2 = True
                break
            else:
                print("You didn't roll a six, try again!")
                break
        else:
            print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
            continue
    return player_2_box, start2, starter2

def player_2_game(player_2_box):
    while True:
        roll = input('Press "r" to roll the dice: ')
        if roll == 'r':
            rolled = random.randint(1,6)

            total_rolled = super_roll(rolled)
            rolled = total_rolled
            time.sleep(1)
            print(f"You rolled {rolled}")

            player_2_box = movement_of_player_1(player_2_box,rolled)
            time.sleep(1)
            print(f"You are now in box {player_2_box}")

            #possible ladders to climb
            if player_2_box ==  7:
                ladder_1()
                player_2_box = 25

            elif player_2_box ==  11:
                ladder_2()
                player_2_box = 87

            elif player_2_box ==  3:
                ladder_3()
                player_2_box= 35

            elif player_2_box ==  16:
                ladder_4()
                player_2_box = 58

            elif player_2_box ==  49:
                ladder_5()
                player_2_box = 70


            #possible snakes
            if player_2_box == 97:
                snake_1()
                player_2_box = 2

            elif player_2_box == 81:
                snake_2()
                player_2_box = 50

            elif player_2_box == 20:
                snake_3()
                player_2_box = 12

            elif player_2_box == 77:
                snake_4()
                player_2_box = 40

            elif player_2_box == 44:
                snake_5()
                player_2_box = 21

            elif player_2_box == 30:
                snake_6()
                player_2_box = 10
            break
                            
                            
        else:
            print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
            continue
    return player_2_box

def player_3_game(player_3_box):
    while True:
        roll = input('Press "r" to roll the dice: ')
        if roll == 'r':
            rolled = random.randint(1,6)

            total_rolled = super_roll(rolled)
            rolled = total_rolled
            time.sleep(1)
            print(f"You rolled {rolled}")

            player_3_box = movement_of_player_2(player_3_box,rolled)
            time.sleep(1)
            print(f"You are now in box {player_3_box}")

            #possible ladders to climb
            if player_3_box  ==  7:
                ladder_1()
                player_3_box  = 25

            elif player_3_box  ==  11:
                ladder_2()
                player_3_box  = 87

            elif player_3_box  ==  3:
                ladder_3()
                player_3_box = 35

            elif player_3_box  ==  16:
                ladder_4()
                player_3_box  = 58

            elif player_3_box  ==  49:
                ladder_5()
                player_3_box  = 70


            #possible snakes
            if player_3_box  == 97:
                snake_1()
                player_3_box  = 2

            elif player_3_box  == 81:
                snake_2()
                player_3_box  = 50

            elif player_3_box  == 20:
                snake_3()
                player_3_box  = 12

            elif player_3_box  == 77:
                snake_4()
                player_3_box  = 40

            elif player_3_box == 44:
                snake_5()
                player_3_box  = 21

            elif player_3_box  == 30:
                snake_6()
                player_3_box = 10
            break
                            
                            
        else:
            print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
            continue
    return player_3_box    

def player_3_start(player_3_box, starter3):
    start3 = False
    if starter3 == 6:
        start3 = True
    while not start3:
        print(f'You are in box number {player_3_box}.')
        roll = input('Press "r" to roll the dice: ')
        if roll == 'r':
            rolled = random.randint(1,6)
            print(f'You rolled {rolled}')
            if rolled == 6:
                player_3_box += 1
                print(f'Welcome you are in box {player_3_box}')
                starter3 = 6
                start3 = True
                break
            else:
                print("You didn't roll a six, try again!")
                break
        else:
            print("To roll the dice you have to press 'r' and hit enter! \nNo other key will is accepted!")
            continue
    return player_3_box, start3, starter3

def one_player():
    player_list =[]
    player_1 =[]
    player_2=[]
    player_1_box = 0
    player_2_box = 0
    starter1 = 0
    starter2 = 0 
    player_1_name = input('Enter player name: ').capitalize().strip()
    computer_name = ['C','o','m','p','u','t','e','r']
    print('Enter player 2 name: ', end ='')
    for item in computer_name:
        print(f"{item}", end = '')
        time.sleep(0.5)
    print()
    player_2_name = 'Computer'
    player_1.append([player_1_name, player_1_box])
    player_2.append([player_2_name, player_2_box])
    player_list.append(player_1)
    player_list.append(player_2)
    time.sleep(3)
    clear_screen()
    while True:
        
        #iterate through the players to ensure each player has a turn
        for player in player_list:
            print(f"Current stats:")
            time.sleep(0.5)
            print(f"{player_1_name : <5}: {player_1_box}")
            time.sleep(0.5)
            print(f"{player_2_name : <5}: {player_2_box}")
            print()
            print(f"{player[0][0]}'s turn")
            print()
            if player[0][0] == player_1_name :
                player_1_box , start1, starter1 = player_1_start(player_1_box, starter1)

            if player[0][0] == player_1_name and start1 == True:
               player_1_box = player_1_game(player_1_box)
            if player_1_box == 100:
                print(f"Congratulations {player_1_name}, you won✨🎉✨🎉✨🎉✨🎉")
                print()
                break

            if player[0][0] == player_2_name:
                player_2_box , start2, starter2 = player_2_start_computer(player_2_box, starter2)

            if player[0][0] == player_2_name and start2 == True :
                player_2_box = player_2_game_computer(player_2_box)
            if player_2_box >= 100:
                print(f"Congratulations {player_2_name}, you won✨🎉✨🎉✨🎉✨🎉")
                print()
                break

            time.sleep(3)
            clear_screen()


def two_player():
    player_list =[]
    player_1 =[]
    player_2=[]
    player_1_box = 0
    player_2_box = 0
    starter1 = 0
    starter2 = 0 
    player_1_name = input('Enter player 1 name: ').capitalize().strip()
    player_2_name = input('Enter player 2 name: ').capitalize().strip()
    player_1.append([player_1_name, player_1_box])
    player_2.append([player_2_name, player_2_box])
    player_list.append(player_1)
    player_list.append(player_2)
    time.sleep(3)
    clear_screen()
    while True:
        #to check if no one has won yet
        
        

        #iterate through the players to ensure each player has a turn
        for player in player_list:
            print(f"Current stats: \n{player_1_name : <5}: {player_1_box} \n{player_2_name : <5}: {player_2_box} \n")
            print(f"{player[0][0]}'s turn")
            print()
            if player[0][0] == player_1_name:
                player_1_box , start1, starter1 = player_1_start(player_1_box, starter1)
                   
            if player[0][0] == player_2_name:
                player_2_box , start2, starter2 = player_2_start(player_2_box, starter2)
               
            if player[0][0] == player_1_name and start1 == True:
               player_1_box = player_1_game(player_1_box)
            if player_1_box == 100:
                print()
                print(f"Congratulations {player_1_name}, you won✨🎉✨🎉✨🎉✨🎉")
                break

            if player[0][0] == player_2_name and start2 == True :
                player_2_box = player_2_game(player_2_box)
            if player_2_box == 100:
                print()
                print(f"Congratulations {player_2_name}, you won✨🎉✨🎉✨🎉✨🎉")
                break

            #managing the terminal by pausing for 3 seconds and then clearing the screen
            time.sleep(3)
            clear_screen()
                
        
def three_player():
    player_list =[]
    player_1 =[]
    player_2=[]
    player_3=[]
    player_1_box = 0
    player_2_box = 0
    player_3_box = 0
    starter1 = 0
    starter2 = 0 
    starter3 = 0 
    player_1_name = input('Enter player 1 name: ').capitalize().strip()
    player_2_name = input('Enter player 2 name: ').capitalize().strip()
    player_3_name = input('Enter player 3 name: ').capitalize().strip()
    player_1.append([player_1_name, player_1_box])
    player_2.append([player_2_name, player_2_box])
    player_3.append([player_3_name, player_3_box])
    player_list.append(player_1)
    player_list.append(player_2)
    player_list.append(player_3)
    time.sleep(3)
    clear_screen()
    while True: #the loop of the whole game

        #iterate through the players to ensure each player has a turn
        for player in player_list:

            print(f"Current stats: \n{player_1_name : <5}: {player_1_box} \n{player_2_name : <5}: {player_2_box} \n{player_3_name : <5}: {player_3_box} \n")
            print(f"{player[0][0]}'s turn")
            print()
            if player[0][0] == player_1_name:
                player_1_box , start1, starter1 = player_1_start(player_1_box, starter1)
                   
            if player[0][0] == player_2_name:
                player_2_box , start2, starter2 = player_1_start(player_2_box, starter2)
            
            if player[0][0] == player_3_name:
                player_3_box , start3, starter3 = player_3_start(player_3_box, starter3)
               

            if player[0][0] == player_1_name and start1 == True:
               player_1_box = player_1_game(player_1_box)
            if player_1_box == 100:
                print()
                print(f"Congratulations {player_1_name}, you won✨🎉✨🎉✨🎉✨🎉")
                player_list.remove(player_1)
                    
            if player[0][0] == player_2_name and start2 == True :
                player_2_box = player_2_game(player_2_box)
            if player_2_box == 100:
                print()
                print(f"Congratulations {player_2_name}, you won✨🎉✨🎉✨🎉✨🎉")
                player_list.remove(player_2)

            if player[0][0] == player_3_name and start3 == True :
                player_3_box = player_3_game(player_3_box)
            if player_3_box == 100:
                print()
                print(f"Congratulations {player_3_name}, you won✨🎉✨🎉✨🎉✨🎉")
                player_list.remove(player_3)

            
            time.sleep(3)
            clear_screen()
            if len(player_list) < 2 :
                
                break
               
               
while True:                
    players = input('Select the number of players \n1. 1 player \n2. 2 players \n3. 3 players \nTo close press "Q" \n>  ').lower().strip()
    if players == '1' or players == '1 player':
        time.sleep(2)
        clear_screen()
        one_player()

    elif players == '2' or players == '2 player':
        time.sleep(2)
        clear_screen()
        two_player()

    elif players == '3' or players == '3 players':
        time.sleep(2)
        clear_screen()
        three_player()

    elif players == 'q':
        print("Thank you for playing snakes and ladders")
        time.sleep(2)
        clear_screen()
        break

    else:
        print('INVALID INPUT!')
        time.sleep(2)
        clear_screen()
        continue
    

