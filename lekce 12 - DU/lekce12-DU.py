"""Task 1
Supplement the Car class with the ability to pack and unpack data using json and pickle."""
import json
import pickle

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def save_to_json(self, file_name):
        data = {
            "brand": self.brand,
            "model": self.model,
            "year": self.year
        }
        try:
            with open(f"{file_name}.json", "r") as infile:
                cars_list = json.load(infile)
        except FileNotFoundError:
            cars_list = []

        cars_list.append(data)

        with open(f"{file_name}.json", "w") as outfile:
            json.dump(cars_list, outfile, indent=4)

    @staticmethod
    def from_json(file_name):
        with open(file_name) as json_file:
            cars_data = json.load(json_file)
        return [Car(car["brand"], car["model"], car["year"]) for car in cars_data]

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"


cars = [Car("BMW", "i7", 2024),
        Car("Audi", "R8", 2017),
        Car("Škoda", "Octavia", 2024)]

for car in cars:
    car.save_to_json("cars") # output cars.json

# Load all cars from JSON
cars_from_json = Car.from_json("cars.json")
for car in cars_from_json:
    print(car)



"""Task 2
Create a class containing a set of integers. The class should have the following functionality implemented:
The sum of elements in the set.
Arithmetic mean of elements in the set.
Maximum of the elements in the set.
Minimum of the elements in the set.
Test all the possibilities of the created class using unit testing (unittest)."""


