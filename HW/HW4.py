class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
    def fill(self, milliliters):
        self.milliliters = milliliters
        if self.quantity + self.milliliters <=self.size:
            self.quantity += self.milliliters
    def status(self):
        return self.size - self.quantity
cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())  
