"""
Task 2
Develop a game of Bulls and Cows. The program chooses a four-digit number,
and the player has to guess it. After the user enters a number,
the program reports how many digits of the number are guessed (bulls),
and how many digits are guessed and stand in the right place (cows). After guessing the number,
print the number of user's attempts. Use recursion in your game.
"""

import random

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def unique_4_digit_number():
    random.shuffle(digits)
    while digits[0] == 0:
        random.shuffle(digits) # Vím, že by to šlo udělat lépe, vygenerovat 1. číslici zvlášť bez 0 a pak spojit
    secret = ''.join(map(str, digits[:4]))  # Select the first 4 digits and combine them into one number
    return secret # output str

def print_main_menu():
    print("""
---Game of Bulls and Cows---
   I think a 4-digit number. Can you guess which one it is?
----------------------------
""")

def bad_input_message():
    print("Bad input. Please try again!")

"""

"""
def count_bulls(secret, guess, bulls=0, cut_secret='', cut_guess=''):
    if not secret:
        return bulls, cut_secret, cut_guess
    if secret[0] == guess[0]:
        return count_bulls(secret[1:], guess[1:], bulls + 1, cut_secret, cut_guess)
    else:
        cut_secret += secret[0]
        cut_guess += guess[0]
        return count_bulls(secret[1:], guess[1:], bulls, cut_secret, cut_guess)

def count_cows(cut_secret, cut_guess, cows=0):
    for j in range(0, len(cut_guess)):
        if cut_guess[j] in cut_secret:
            cows += 1
    return cows

print_main_menu()
secret = unique_4_digit_number()
i = 1
while True:
    print(f"Secret number for debugging: {secret}")
    guess = input("Guess a 4-digit number: ")

    if not guess.isdigit() or len(guess) != 4:
        bad_input_message()
        continue

    bulls, cut_secret, cut_guess = count_bulls(secret, guess)
    cows = count_cows(cut_secret, cut_guess)
    print(f"Bulls: {bulls}, Cows: {cows}")

    if bulls == 4:
        print(f"Congratulations! You guessed the number {secret}.")
        print(f"Number of trials: {i}")
        break
    i += 1