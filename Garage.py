from Vehicle import Car
from Vehicle import Vehicle

class Garage:

    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        if not isinstance(car, Car):
            raise TypeError("Only Car objects can be added to the garage.")
        self.cars.append(car)

    def remove_car(self, car: Car):
        if car in self.cars:
            self.cars.remove(car)
        else:
            raise ValueError("Car not found in the garage")

    def list_cars(self):
        print(f"Number of cars in garage: {len(self.cars)}")
        for car in self.cars:
            print(car.get_model())
        
    def get_car(self, model: str):
        for car in self.cars:
            if car.get_model() == model:
                print(f"Car found: {car.get_model()}")
                return car
        if car.get_model() != model:
            print(f"Car with model {model} not found in the garage.")
        #raise ValueError(f"Car with model {model} not found in the garage.")
    
    def save_to_file(self, filename: str):
        with open(filename, 'w') as file:
            for car in self.cars:
                file.write(f"{car.get_model()},{car.get_horsepower()},{car.get_weight()},{car.get_drivetrain()}\n")
    
    def load_from_file(self, filename: str):
        self.cars = []
        with open(filename, 'r') as file:
            for line in file:
                model, horsepower, weight, drivetrain = line.strip().split(',')
                car = Car(model, int(horsepower), float(weight), drivetrain)
                self.add_car(car)

# test the Garage class
camaro = Car('camaro', 275, 3200, 'rwd')
challenger = Car('challenger', 305, 3400, 'rwd')
mustang = Car('mustang', 310, 3300, 'rwd')
garage = Garage()
garage.add_car(camaro)
garage.add_car(challenger)
garage.add_car(mustang)
# garage.list_cars()
garage.get_car('charger')