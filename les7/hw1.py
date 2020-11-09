class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list


    def __str__(self):
        result = ""
        for el in self.my_list:
            result1 = ""
            for i in str(el):
                result1 += i + ""
            result += result1 + "\n"
        return result

    def __add__(self, other):

        result = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

        for i in range(len(self.my_list)):

            for j in range(len(self.my_list[0])):
                result[i][j] = self.my_list[i][j] + other.my_list[i][j]
        """Так и не удалось придумать, как сделать это в add"""



mc = [[1, 2, 3] ,[4, 5, 6], [7, 8, 9]]
ma = [[11, 22, 33] ,[44, 54, 66],[77, 88, 99]]
print(result)