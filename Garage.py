from ClassVehicle import Car

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
        return [car.get_model() for car in self.cars]
    
    def get_car(self, model: str):
        for car in self.cars:
            if car.get_model() == model:
                return car
        raise ValueError(f"Car with model {model} not found in the garage.")
    
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
