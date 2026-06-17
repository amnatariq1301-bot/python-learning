class car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyota_car(car):
    def __init__(self, brand ):
        self.brand  = brand

class fortuner(toyota_car):
    def __init__(self, type):
        self.type = type

car1 = car()
print(car1.start())