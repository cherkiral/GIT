from my_module import list_creation

my_list = list_creation()
my_sorted_list = [elem for elem in my_list if my_list.count(elem) == 1]
print(my_sorted_list)