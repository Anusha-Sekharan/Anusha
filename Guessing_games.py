'''import random
print("Hello welcome to guessing game.\n You have to guess a number between 1 and 100.\n You have 10 chances to guess the number.")
num_to_guess=random.randint(1,100)
chances=10
guess_counter=0
while guess_counter<chances:
  guess_counter+=1
  my_guess=int(input("Enter your gueess"))
  if my_guess==num_to_guess:
    print(f"Congratulations.The guessed number is correct. You foundn it in {guess_counter} attempt")
    break
  elif my_guess<num_to_guess:
    print("Your guess is too low!")
  elif my_guess>num_to-guess:
    print("Your guess is too high!")
  elif guess_counter>=num_to_guess:
    print(f"Sorry you have run out of guesses. The number is {num_to_guess}. BETTER LUCK NEXT TIME!")
    break'''

import random

def welcome_display():
  print("Welcome to the GUESSING GAME.\n You have to guess a number between 1 and 100.\n You have 5 to 10 chances based on your difficulty level.\n ALL THE BEST!")


def get_difficulty():
  difficulty = input(
      "Enter your difficulty level (easy/medium/hard) :").lower()
  if difficulty == "easy":
    return 10
  elif difficulty == "medium":
    return 7
  elif difficulty == "hard":
    return 5
  else:
    print("INVALID INPUT. PLEASE ENTER A VALID INPUT")
    return get_difficulty()


def guess_game():
  welcome_display()
  chances = get_difficulty()
  num_to_guess = random.randint(1, 100)
  guess_counter = 0
  while guess_counter < chances:
    guess_counter += 1
    try:
      my_guess = int(input("Enter your guess:"))
    except ValueError:
      print("INVALID NUMBER. PLEASE ENTER A VALID NUMBER.")
      guess_counter -= 1
      continue

    if my_guess == num_to_guess:
      print(
          f"CONGRATULATIONS. You have guessed the number correctly. You found it in {guess_counter} attempts."
      )
      break
    elif my_guess < num_to_guess:
      print("Your guess is too low!")
    elif my_guess > num_to_guess:
      print("Your number is too high!")

    if guess_counter == chances:
      print(
          f"Sorry you have run out of guesses.\n The number is {num_to_guess}. \n BETTER LUCK NEXT TIME"
      )
      break


if __name__ == "__main__":
  guess_game()
