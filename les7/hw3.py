class Cell():
    def __init__(self, amount_of_cells: int):
        self.amount_of_cells = amount_of_cells

    def __add__(self, other):
        return self.amount_of_cells + other.amount_of_cells

    def __sub__(self, other):
        if self.amount_of_cells - other.amount_of_cells > 0:
            return self.amount_of_cells - other.amount_of_cells
        else:
            return "Incorrect input"

    def  __mul__(self, other):
        return self.amount_of_cells * other.amount_of_cells

    def __truediv__(self, other):
        return float(self.amount_of_cells / other.amount_of_cells)

    def make_order(self, amount_in_string):
        result = ""
        amount_of_rows = self.amount_of_cells // amount_in_string
        remains = self.amount_of_cells % amount_in_string
        while amount_of_rows > 0:
            result = result + "*" * amount_in_string + '\n'
            amount_of_rows -= 1
        if remains > 0:
            result = result + "*" * remains

        return result

cell1 = Cell(2)
print(Cell.make_order(cell1, 5))











