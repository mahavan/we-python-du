"""
Task 1
Create a Ship class containing information about a ship.
Use inheritance to implement a Frigate class (contains info about a frigate), a Destroyer class (contains info
about a destroyer), a Cruiser class (contains info about a cruiser).
Each class must have the required methods.
"""
class Ship:
    def __init__(self, name):
        self.name = name
    def menu(self):
        print("Information about ships:")
        print(self.name)

class Frigate(Ship):
    def main_role(self):
        print("Frigate: Anti-submarine warfare, convoy escort.")

class Destroyer(Ship):
    def main_role(self):
        print("Destroyer: Anti-air and anti-submarine defense.")

class Cruiser(Ship):
    def main_role(self):
        print("Cruiser: Fleet command, heavy firepower.")

f1 = Frigate("HMS Montrose (UK)")
f1.menu()
f1.main_role()
print()
d1 = Destroyer("HMS Defender (UK)")
d1.menu()
d1.main_role()
print()
c1 = Cruiser("USS Ticonderoga (USA)")
c1.menu()
c1.main_role()
print()


"""
Task 2
Create a function to display the current time. The function takes no parameters. 
Decorate the function using another function without utilizing decorator syntax. Possible output:

***************************
23:00
***************************

Two lines of asterisks here are the result of the decoration.
"""


"""
Task 3
Do Task 2 using decorator syntax.
"""

"""
Task 4
Create a pizza maker app. Each pizza has different ingredients. Use decorators to create different pizzas:
Margarita;
Four cheese;
Capricciosa;
Hawaiian.
"""

