"""
Task 2
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

    def save_to_pickle(self, file_name):
        try:
            with open(f"{file_name}.pkl", "rb") as infile:
                cars_list = pickle.load(infile)
        except FileNotFoundError:
            cars_list = []

        cars_list.append(self)

        with open(f"{file_name}.pkl", "wb") as outfile:
            pickle.dump(cars_list, outfile)

    @staticmethod
    def from_pickle(file_name):
        with open(file_name, "rb") as pickle_file:
            cars_data = pickle.load(pickle_file)
        return cars_data

cars = [Car("BMW", "i7", 2024),
        Car("Audi", "R8", 2017),
        Car("Škoda", "Octavia", 2024)]

for car in cars:
    car.save_to_json("cars") # output cars.json

# Load all cars from JSON
cars_from_json = Car.from_json("cars.json")
print("Cars from JSON file:")
for car in cars_from_json:
    print(car)

for car in cars:
    car.save_to_pickle("cars")  # output cars.pkl

# Load all cars from pickle
cars_from_pickle = Car.from_pickle("cars.pkl")
print()
print("Cars from pkl file:")
for car in cars_from_pickle:
    print(car)



