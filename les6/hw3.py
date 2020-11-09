class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]



a = Position(input('Input your name\n'), input('Input your surname\n'), input('Input your position\n'),
             {"wage": float(input("Input your wage\n")), "bonus": float(input('Input your bonus\n'))})
print (a.get_full_name())
print(a.get_total_income())