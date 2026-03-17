class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model} engine started."

    def move(self):
        return f"{self.brand} {self.model} is moving."

    def __str__(self):
        return f"Vehicle: {self.brand} {self.model} ({self.year})"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def move(self):
        return f"Car {self.brand} {self.model} is driving."

    def honk(self):
        return "Beep!"


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def move(self):
        return f"Motorcycle {self.brand} {self.model} is driving."

    def wheelie(self):
        return f"{self.brand} {self.model} is doing a wheelie!"