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
bulls = 0
cows = 0

def unique_4_digit_number():
    random.shuffle(digits)
    while digits[0] == 0:
        random.shuffle(digits)
    number = int(''.join(map(str, digits[:4])))  # Select the first 4 digits and combine them into one number
    return number

def print_main_menu():
    print("""
---Game of Bulls and Cows---
   I think a 4-digit number. Can you guess which one it is?
   Input 4-digit number.
-------------------------------       
""")

def bad_input_message():
    print("Zadal(a) jsi neplatné číslo!")

def run_game():
    users_number = int(input())
    if users_number.isdigit() and len(users_number) == 4:

    else:
        bad_input_message()

print(f"Bulls: {bulls}, Cows: {cows}")
print(f"Počet pokusů: {i}")
