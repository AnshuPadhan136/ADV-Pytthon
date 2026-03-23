class Vehicle:
    def rent(self):
        pass

class Car(Vehicle):
    def rent(self): return 100

class Bike(Vehicle):
    def rent(self): return 50

class Truck(Vehicle):
    def rent(self): return 200