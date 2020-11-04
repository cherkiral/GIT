class Road:
    spec_mass = 25
    thickness = 5

    def __init__(self, _width, _length):
        self._length = _length
        self._width = _width

    def mass(self):
        return (self._length * self._width * self.spec_mass * self.thickness) / 1000
a = Road(20, 5000)
print(a.mass())
