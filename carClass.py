class Car:

    def __init__(self, model = "Toyota Camry", hp = 151, engine = "V6", zeroSixty = 5.7):
        self.model = model
        self.hp = hp
        self.engine = engine
        self.zeroSixty = zeroSixty



    def whatCar(self):
        print(f"Stats:\n Model: {self.model}, HP: {self.hp}, Engine: {self.engine}, 0-60: {self.zeroSixty}")

    def setModel(self, model):
        self.model = model

    def getModel(self):
        return self.model

    def setHP(self, hp):
        self.hp = hp

    def getHP(self):
        return self.hp

    def setEngine(self, engine):
        self.engine = engine

    def getEngine(self):
        return self.engine

    def setZeroSixty(self, zeroSixty):
        self.zeroSixty = zeroSixty

    def getZeroSixty(self):
        return self.zeroSixty
