"""
Task 1
Implement a class Car. Class fields should store the following: model, year of release, manufacturer, engine capacity,
color, price. Implement class methods for data input and output, provide access to individual fields through class
methods.
"""

class Car:
    def __init__(self, manufacturer, model, year, engine_capacity, color, price):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def __str__(self):
        return f"Car: {self.manufacturer} {self.model} {self.year} - capacity: {self.engine_capacity}, color: {self.color}, price: {self.price}"

car1 = Car("Toyota", "Corolla", 2020, 1.8, "white", "$20,000")
car2 = Car("Ford", "Mustang", 2022, 5.0, "red", "$45,000")
car3 = Car("Audi", "A4", 2023, 2.0, "silver", "$40,000")

print(car1)
print(car2)
print(car3)

"""
Task 2
Create a class to convert temperature from Celsius to Fahrenheit, and vice versa. The class must have two static methods: 
to convert from Celsius to Fahrenheit and from Fahrenheit to Celsius. The class should also count how many times 
the temperature was calculated and return this value using a static method.
"""