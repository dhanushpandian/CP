class Car:
    # self.make=None
    # self.model=None
    # self.year=None
    # self.color=None
    def __init__(self, brand=None, model=None, year=None, color=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping")

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"