class Car:
    def __init__(self, marka, model, year, skorost = 0):
        self.marka = marka
        self.model = model
        self.year = year
        self.skorost = skorost

    def skor(self):
        return self.skorost + 5

    def skor2(self):
        return self.skorost - 5

    def stop(self):
        return self.skorost - self.skorost

    def now(self):
        return self.skorost

    def ret(self):
        return self.skorost * (-1)

d1 = Car("a100", "AA", 2015, 45)
print(d1.ret())