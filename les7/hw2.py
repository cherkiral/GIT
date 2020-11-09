class Clothes():
    def __init__(self, brand):
        self.brand = brand


class Coat(Clothes):

    def __init__(self, brand, size: float):
        self.size = size
        super().__init__(brand)

    def cloth_spent(self):
        return f"Cloth spent on {self.brand} coat: {self.size / 6.5 + 0.5}"


class Suit(Clothes):
    def __init__(self, brand, size: float):
        self.size = size
        super().__init__(brand)

    def cloth_spent(self):
        return f"Cloth spent on {self.brand} suit: {self.size * 2 + 0.3}"


a = Coat("ZARA", 44).cloth_spent()
b = Suit("H & M", 44).cloth_spent()