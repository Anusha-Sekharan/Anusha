import random
import streamlit as st

def welcome_display():
    st.title("Welcome to the GUESSING GAME!")
    st.write("Guess a number between 1 and 100.")
    st.write("You will have 5 to 10 chances based on your difficulty level.")
    st.write("Good Luck!")

def get_difficulty():
    difficulty = st.selectbox("Choose your difficulty level:", ["easy", "medium", "hard"])
    if difficulty == "easy":
        return 10
    elif difficulty == "medium":
        return 7
    elif difficulty == "hard":
        return 5

def guess_game():
    welcome_display()
    chances = get_difficulty()
    num_to_guess = random.randint(1, 100)
    guess_counter = 0

    while guess_counter < chances:
        guess_counter += 1
        my_guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
        
        if my_guess:
            if my_guess == num_to_guess:
                st.success(f"CONGRATULATIONS! You guessed the number correctly in {guess_counter} attempts.")
                break
            elif my_guess < num_to_guess:
                st.warning("Your guess is too low!")
            elif my_guess > num_to_guess:
                st.warning("Your guess is too high!")

        if guess_counter == chances:
            st.error(f"Sorry, you've run out of guesses. The number was {num_to_guess}. Better luck next time!")

if __name__ == "__main__":
    guess_game()
