from Vehicle import Car

class Simulation:

    def zero_to_sixty(self, car: Car):
        time = car.__horsepower / car._weight
        return f"0-60 mph in {time} seconds."
    
    def quarter_mile_time(self, car: Car):
        quarter_time = time / 4
        return f"quarter mile time: {quarter_time} seconds."
    
    def compare(self, car1: Car, car2: Car):
        car1_time = car1.__horsepower / car1._weight
        car2_time = car2.__horsepower / car2._weight
        if car1_time > car2_time:
            print('{car1} has a faster 0-60 time.')
        else:
            print('{car2} has a faster 0-60 time.')

