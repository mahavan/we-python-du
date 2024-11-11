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
        random.shuffle(digits)
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


def compare_digits_recursive(secret, guess, bulls=0, cows=0, cows_counting=0, str_bulls=''):
    """
    Rekurzivně porovnává tajné číslo a uživatelský odhad.
    Vrací počet Bulls (správné číslice na správné pozici)
    a Cows (správné číslice na špatné pozici).
    """
    # Základní případ: Pokud jsme dosáhli konce řetězců
    if not secret:
        return bulls, cows

    # Kontrola Bulls
    if secret[0] == guess[0]:
        str_bulls += secret[0]
        print(f"str_bulls: {str_bulls}")
        return compare_digits_recursive(secret[1:], guess[1:], bulls + 1, cows, cows_counting, str_bulls)

    else:
        if not cows_counting:
            # Kontrola Cows
            for j in range(0, len(guess)):
                if guess[j] in secret:
                    cows += 1
                    print(len(guess),guess[j], j, cows)
                else:
                    print(guess[j], cows_counting)
            return compare_digits_recursive(secret[1:], guess[1:], bulls, cows, cows_counting + 1, str_bulls)
        else:
            return compare_digits_recursive(secret[1:], guess[1:], bulls, cows, cows_counting, str_bulls)

# Hlavní část programu
print_main_menu()
secret = unique_4_digit_number()

i = 1  # Počítadlo pokusů
while True:
    print(f"(Secret number for debugging: {secret})")  # Pro testování
    guess = input("Guess a 4-digit number: ")

    # Kontrola platnosti vstupu
    if not guess.isdigit() or len(guess) != 4:
        bad_input_message()
        continue

    # Spočítáme Bulls a Cows pomocí rekurzivní funkce
    bulls, cows = compare_digits_recursive(secret, guess)
    print(f"Bulls: {bulls}, Cows: {cows}")

    # Kontrola, zda uživatel uhodl správně
    if bulls == 4:
        print(f"Congratulations! You guessed the number {secret}.")
        print(f"Number of trials: {i}")
        break

    i += 1  # Zvýšení počítadla pokusů