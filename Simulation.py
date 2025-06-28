from Vehicle import Vehicle, Car


class Simulation:

    def zero_to_sixty(self, car: Car):
        time = car.get_horsepower() / car.get_weight()
        return f"0-60 mph in {time} seconds."
        if not ininstance(car, Car):
            raise TypeError("Expected a Car instance.")
    
    def quarter_mile_time(self, car: Car):
        quarter_time = (car.get_horsepower() / car.get_weight()) / 4
        return f"quarter mile time: {quarter_time} seconds."
    
    def compare(self, car1: Car, car2: Car):
        car1_time = car1.get_horsepower / car1.get_weight
        car2_time = car2.get_horsepower / car2.get_weight
        if car1_time > car2_time:
            print(f'{car1.get_model()} has a faster 0-60 time.')
        else:
            print(f'{car2.get_model()} has a faster 0-60 time.')

