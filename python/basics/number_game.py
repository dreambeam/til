import random
#generate a random number 1 to 10
secret_num = random.randint(1,10)

def game():
  trial =3

  while trial!=0:
    try:
      #get a number from the player safely
      guess = int(input("Enter your guess> "))
    
    except ValueError:
      print("Your input {} is not a number ".format(guess))    

    #compare number
    if guess == secret_num:
      print("That's it . You got it right {}".format(secret_num))
      break
  
    else:
      trial=trial -1
      if trial!=0:
        print("That's not it ! Try again ")
        #if they dont get it right do something tell them or hint
        if guess<= secret_num:
          print("My number is higher than {} ".format(guess))
        else:
          print("My number is lower than {} ".format(guess))
        
      else:
        #game over after 3 trial: limiting the guesses
        print("Game over !! ")
        print("My number was was {} ".format(secret_num))

  else:
    #play again
    play_again =input("Do you you wanna play again ? (Y/n) ")
    if play_again.lower()!='n':
      game()

game()


#limit guess;
#guesses=[]
#while len(guesses<5)