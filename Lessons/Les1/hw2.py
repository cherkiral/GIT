from my_module import list_creation
my_list = list_creation()
my_new_list = [elem for position, elem in enumerate(my_list[1:], 1) if my_list[position] > my_list[position - 1]]
print(my_new_list)
