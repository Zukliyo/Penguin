import random
hngmn = ['''
             
                +---+
                |   |
                    |
                    |
                    |
                    |
              =========''', 
  '''
             
                +---+
                |   |
                O   |
                    |
                    |
                    |
              =========''', 
  '''
             
                +---+
                |   |
                O   |
                |   |
                    |
                    |
              =========''',
   '''
             
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
              =========''',
    '''
             
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
              =========''',
     '''
             
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
              =========''',
     '''
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
              =========''']

hanged_man = '''
                +---+
                |   |
               _O_  |
                |   |
               / \  |
                    |
              ========='''

free_man = ['''
                +---+
                    |
                    |
               _O_  |
                |   |
               | |  |
              =========''',
    '''
                +---+
                    |
                    |
               \O/  |
                |   |
               | |  |
              ========='''
            ]
words = [
  'apple','Giggle', 'Scissors','Guitar',
  'juice','Cat','Golf','Skip','Chicken'
  'Sneeze','Chimpanzee','Hammer','Airplane',
  'Angry','Baby','Ball','Baseball','Bounce',
  'Basketball','Spin','Clap','Happy','Spoon',
  'Cough','Horns','Stomp','Cry','Joke','Stop',
  'Dog','Mime','Tail','Drink','Penguin','Toothbrush',
  'Drums','Phone','Wiggle','Duck',
  ]

let = list('qwertyuiopasdfghjklzxcvbnm')


while True:
  lvl = input('Hard, medium or easy?[h/m/e]')
  if lvl == 'h' or lvl == 'm' or lvl == 'e':
    break

random_word = random.choice(words)
lword = list(random_word)
lline = list('_' * len(lword))
# print(random_word)

count = 0
if lvl == 'h':
  print("Oh really? hard one? Okay, Let's goooo!")
  loss = len(lline) + 6
elif lvl == 'm':
  print('You chose medium level, good luck!')
  loss = len(lline) + 11
elif lvl == 'e':
  print('You chose easy way, have fun!')
  loss = len(lline) + 20

print(' '.join(lline), '\n')

while True:
  user = input('Guess the letter:  ')
  if user in lline:
    print('Already guessed\n')

  elif user not in let:
    print('Already Entered this letter\n')

  elif user in lword:
    let.remove(user)
    for index, item in enumerate(lword):
      if user == item:
        lline[index] = user
    print(' '.join(lline))
    count += 1

  else:
    if user in let:
      let.remove(user)
      loss -= 1
      print(f'Incorrect letter, tries left:{loss}\n')
      
      # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   if you want to see hangman, just uncomment code below   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
      
      # try:
      #   print(hngmn[0])
      #   del hngmn[0]
      #   if hngmn == []:
      #     print('You lost')
      #     break
      # except:
      #   pass
      

  if count == len(lline):
    print('Great job!')
    break
  if loss == 0:
    print('You lost!')
    break

