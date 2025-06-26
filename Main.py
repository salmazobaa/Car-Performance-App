# car OOP project

class Vehicle:

    def __init__(self, model, weight):
        self.model = model
        self.weight = weight

    def get_model(self):
        return self.model

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight: float):
        self.weight = new_weight

        if not isinstance(new_weight, (int, float)):
            raise TypeError(f"{new_weight} must be a number.")

        assert new_weight >= 0, f"{new_weight} must be bigger than zero."

    def describe(self):
        pass 


class Car(Vehicle):

    def __init__(self, model: str, horsepower: int, weight: float, drivetrain: str):
        super().__init__(model, weight)
        self.horsepower = horsepower
        self.drivetrain = drivetrain

    def get_horsepower(self):
        return self.horsepower

    def set_horsepower(self, new_horsepower: int):
        self.horsepower = new_horsepower

        if not isinstance(new_horsepower, int):
            raise TypeError(f"{new_horsepower} must be an integer.")

        assert new_horsepower >= 0, f"{new_horsepower} must be bigger than zero."
    
    def get_drivetrain(self):
        return self.drivetrain

    def set_drivetrain(self, new_drivetrain: str):
        self.drivetrain = new_drivetrain

        if not isinstance(new_drivetrain, str):
            raise TypeError(f"{new_drivetrain} must be a string.")

        assert new_drivetrain in ['FWD', 'RWD', 'AWD', '4WD'], f"{new_drivetrain} must be one of 'FWD', 'RWD', '4WD' or 'AWD'."
    
    def power_to_weight_ratio(self):
        return self.horsepower / self.weight
    
    def reset_specs(self):
        pass

    def describe(self):
        pass


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

