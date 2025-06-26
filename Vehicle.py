class Vehicle:

    def __init__(self, model, weight):
        self._model = model
        self._weight = weight

    def get_model(self):
        return self._model
    
    def set_model(self, new_model:str):
        self._model = new_model

        if not isinstance(new_model, str):
            raise TypeError(f"invalid model.")

    def get_weight(self):
        return self._weight

    def set_weight(self, new_weight: float):
        self._weight = new_weight

        if not isinstance(new_weight, (int, float)):
            raise TypeError(f"{new_weight} must be a number.")

        assert new_weight >= 0, f"{new_weight} must be bigger than zero."

    def describe(self):
        return f"{self.horsepower}"


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

