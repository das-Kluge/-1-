class Vehicle:
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

    def get_info(self):
        return f"марка: {self.mark}, модель: {self.model}"

class Car(Vehicle):
    def __init__(self, mark, model, fueltype):
        super().__init__(mark, model)
        self.fueltype = fueltype

    def get_info(self):
        vehicle_info = super().get_info()
        return vehicle_info + f", тип топлива: {self.fueltype}"

cara = Vehicle(input('mark '),input('model '))
car = Car(input('mark '), input('model '), input('fuel '))
print(car.get_info())
print(cara.get_info())
