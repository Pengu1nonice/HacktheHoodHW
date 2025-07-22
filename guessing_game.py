# Guessing game - Marvin M

import random

def generate_random_number():
    return random.randint(1,100)

def get_user_guess():
    while True:
        input1 = int (input("guess a number between 1-100:"))
        if input1 >= 1 and input1 <= 100:
            return input1
        else:
            print("the number isn't between 1-100")

def play_guessing_game():
    global secret_number
    guesses = 0
    secret_number = generate_random_number()
    
    while True:
        user_guess = get_user_guess()
        guesses +=1
        if user_guess < secret_number:
            print("your guess is too low")
        elif user_guess > secret_number:
            print("your guess is too high")
        else:
            print(f"your guess is correct. it took you {guesses} tries")
            break

def game_loop():
    while True:
        play_guessing_game()
        input2 = input("would you like to play again?:")
        if input2 == "yes":
            play_guessing_game()
        else:
            break

if __name__ == "__main__": 
    game_loop()