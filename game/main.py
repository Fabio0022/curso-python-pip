import random

def choose_option():
    options = ('piedra', 'papel', 'tijeras')
    user_option = input('piedra, papel o tijera => ').lower()
    # user_option = user_option.lower()
    

    if not user_option in options:
      print('esa no es una opcion validad!')
      #continue
      return None, None
    
    computer_option = random.choice(options)

    print('\n')
    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option
    print('\n')

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Es un empate!')
  elif user_option == 'piedra':
    if computer_option == "tijeras":
      print('piedra gana a tijera')
      print('User gano!')
      user_wins += 1
      print('\n')
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
      print('\n')
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel le gana a piedra')
      print('user gano!')
      user_wins += 1
      print('\n')
    else:
      print('tijera gana a papel')
      print('computer gana')
      computer_wins += 1
      print('\n')
  elif user_option == 'tijeras':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
      print('\n')
    else:
      print('piedra gana a tijeras')
      print('computer gano!')
      computer_wins += 1
      print('\n')
  return user_wins, computer_wins

def run_game():
  user_wins = 0
  computer_wins = 0
  rounds = 1
  while True:
    print('*' * 20)
    print('ROUNDS',rounds)
    print('*' * 20)
    print('Computer wins', computer_wins)
    print('User wins', user_wins)
      
    rounds += 1
      
    user_option, computer_option = choose_option()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
  
    if computer_wins == 2:
      print('El ganador es la computadora!')
      break
    if user_wins == 2:
      print('El ganador es el usuario!')
      break
  
run_game()
  
  