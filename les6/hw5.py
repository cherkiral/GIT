class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start drawing\n")

class Pen(Stationery):
    def draw(self):
        print("Drawing with pen")


class Pencil(Stationery):
    def draw(self):
        print("Drawing with pencil")


class Handle(Stationery):
    def draw(self):
        print("Drawing with handle")

a = Pencil('pencil')
a.draw()
