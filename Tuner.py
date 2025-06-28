from Vehicle import Car, Vehicle

class Tuner:
    
    def increase_horsepower(car: Car, amount: float):
        new_horsepower = car.__horsepower + amount
        if not isinstance (car, Car):
            raise TypeError(f"{car} is not registered.")
        assert amount >= 0, f"amount must be bigger than zero."
        return f"horsepower is now {car.__horsepower}."
    
    def reduce_weight(car:Car, amount:float):
        new_weight = car._weight - amount
        if not isinstance (car, Car):
            raise TypeError(f"{car} is not registered.")
        assert amount >= 0, f"amount must be bigger than zero."
        return f"weight is now {car._weight}"

    def change_drivetrain(car:Car, new_drivetrain: str):
        valid_drivetrains = ['RWD','AWD','FWD', '4WD']
        if new_drivetrain not in valid_drivetrains:
            print(f"{new_drivetrain}is not valid.")
        else:
            car.__drivetrain = new_drivetrain
        return f"drivetrain is now {car.__drivetrain}."
        