import random, os, time
lives = 6

word_dictionary = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
word = random.choice(word_dictionary)
guess = []

def letter_left(word, guess):
  return any(letter not in guess for letter in word)

def clear_screen():
    if os.name == 'posix':
        _= os.system('clear')
    if os.name ==  'nt':
      _=os.system('cls')

def bold(text):
  return f'\033[1m{text}\033[0m'


while True:
  print(bold('HANGMAN'))
  if lives == 6:
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')
  if lives == 5:
    print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')
  if lives == 4:
    print( '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')
  if lives == 3:
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')
  if lives == 2:
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')
  if lives == 1:
    print( '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')
  ask = input('Guess the letters contained in the word: ').lower().strip()
  
  if ask in guess:
    print('You have already tried that before!')
    continue
  guess.append(ask)
  
  if ask in word:
    print('You have found one of the letters!')
  else:
    print('Nope the letter is not in the word')
    lives -= 1
    
  print()
  for i in word:
    if i in guess:
      print(i, end ='')
    else:
      print(' _ ', end='')
  print()
  
  if not letter_left(word, guess):
    print(f'Congratulations you found all the letters! \nYou had {lives} remaining')
    break

  
  if lives == 0:
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
    print(f'You have run out of lives! \nThe word was {word}')
    break
  print(f'You have {lives} remaining')

  time.sleep(5)  
  clear_screen()