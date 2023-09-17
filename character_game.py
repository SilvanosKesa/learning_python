import os, time, random

def health_stat():
  six_sided_roll = random.randint(1,6)
  twelve_sided_roll = random.randint(1,12)
  health = ((six_sided_roll * twelve_sided_roll )/2) + 10
  health = round(health,2)
  return health

def strength_stat():
  six_sided_roll = random.randint(1,6)
  twelve_sided_roll = random.randint(1,12)
  strength = ((six_sided_roll * twelve_sided_roll )/2) + 12
  strength = round(strength,2)
  return strength

def battle():
  if player_1_strength > player_2_strength :
    resultant = (player_1_strength - player_2_strength) + 1
    return resultant
  else:
    resultant = (player_2_strength - player_1_strength) + 1
    return resultant

while True:
  print('Character Builder','\n')
  time.sleep(1)
  #Player 1 information)
  player_1_name= input('What is your name? \n > ')
  time.sleep(1)
  print('\n','Select our character type','\n','human','\n','imp','\n','wizard','\n','elf','\n','Go wild!','\n')
  cha_type1 = input('> ')
  time.sleep(1)
  player_1_health = health_stat()
  player_1_strength = strength_stat()
  print()
  print(player_1_name,'the',cha_type1)
  print('HEALTH: ',player_1_health)
  print('STRENGTH: ',player_1_strength)
  print()
  time.sleep(1)
  print('Who are they battling?','\n')
  #player 2 information
  time.sleep(1)
  player_2_name= input('What is your name? \n > ')
  time.sleep(1)
  print('\n','Select our character type','\n','human','\n','imp','\n','wizard','\n','elf''\n','Go wild !','\n')
  cha_type2 = input('> ')
  time.sleep(1)
  player_2_health = health_stat()
  player_2_strength = strength_stat()
  print()
  print(player_2_name,'the',cha_type2)
  print('HEALTH: ',player_2_health)
  print('STRENGTH: ',player_2_strength)
  time.sleep(10)
  os.system('clear')
  print('BATTLE TIME','\n')
  time.sleep(1)
  count = 0
  while True:
    if player_1_health <= 0:
      time.sleep(1)
      print('Oh no',player_1_name,'the',cha_type1,'has died!','\n')
      print(player_2_name,'destroyed',player_1_name,'in',count,'rounds!')
      time.sleep(10)
      break
    if player_2_health <= 0:
      time.sleep(1)
      print('Oh no',player_2_name,'the',cha_type2,'has died!','\n')
      print(player_1_name,'destroyed',player_2_name,'in',count,'rounds!')
      time.sleep(10)
      break
    else:
      print('BATTLE TIME','\n')
      count += 1
      player_1_roll = random.randint(1,6)
      player_2_roll = random.randint(1,6)
      time.sleep(2)
      if player_1_roll > player_2_roll :
        print(player_1_name,' wins the round')
        player_2_health -= battle()
        print(player_2_name,'takes a hit, with ',battle(),' damage')
      elif player_2_roll > player_1_roll :
        print(player_2_name,' wins the round')
        player_1_health -= battle()
        print(player_1_name,'takes a hit, with ',battle(),' damage')
      else:
        print('This round was a tie')
        os.system('clear')
        continue
      time.sleep(5)
      os.system('clear')
  while True:
    os.system('clear')
    ask =input('Do you want to play again?(yes/no) \n > ')  
    if ask == 'yes':
      os.system('clear')
      break
    elif ask == 'no':
      print('Goodbye!')
      time.sleep(3)
      exit()
    else:
      continue
    