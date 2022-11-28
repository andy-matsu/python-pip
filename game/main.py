import random
round = 1
round += 1
def choose_options():
    option = ("piedra", "papel", "tijera")
    user_option = input("piedra, papel, tijera = ").lower()
     
    if not user_option in option:
      print("te dije piedra papel o tijera imbecil")
      return None, None
      
    computer_option = random.choice(option)
    print("user_option", user_option)
    print("computer_option", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_win, computer_win):
    if user_option == computer_option:
      print("empate")
    elif user_option == "piedra":
      if computer_option == "tijera":
        print("piedra gana a tijera")
        print("computer lose")
        user_win +=1
      else:
        print("papel gana a piedra")
        print("computer win")
        computer_win +=1
    elif user_option == "tijera":
      if computer_option == "papel":
        print("tijera gana a papel")
        print("computer lose")
        user_win +=1
      else:
        print("piedra gana a tijera")
        print("computer win")
        computer_win +=1
    elif user_option == "papel":
      if computer_option == "piedra":
        print("papel gana a piedra")
        print("computer lose")
        user_win +=1
      else:
        print("tijera gana a papel")
        print("computer win")
        computer_win +=1
    return user_win, computer_win
  

def run_game():
  computer_win = 0
  user_win = 0
  round = 1
  while True:
      print("*"* 10)
      print("round", round)
      print("*"* 10)
      round += 1
      print("computer_wins =",computer_win)
      print("user_wins =",user_win)
      print("-------------------")
      user_option, computer_option = choose_options()
      user_win, computer_win = check_rules(user_option, computer_option, user_win, computer_win)
      
      if computer_win == 2:
        print("gana la maquina!! como te quedo el ojo?")
        break
      if user_win == 2:
        print("gana el humano, venciendo nuevamente a la maquina")
        break

run_game()
  
 
   