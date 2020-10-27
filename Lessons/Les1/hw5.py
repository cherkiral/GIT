from my_module import list_multiply
from functools import reduce
my_list = [elem for elem in range(100, 1001) if elem % 2 == 0]
print(reduce(list_multiply, my_list))
