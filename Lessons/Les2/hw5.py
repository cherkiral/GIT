my_list = [7, 5, 3, 3, 2]
choice = "+"
while choice == "+":
    new = int(input("Введите число\n>"))
    my_list.append(new)
    print(sorted(my_list, reverse = True))
    choice = input("Хотите ввести новый элемент рейтинга?\n>")
    my_list.remove(new)

else:
    print('Новых элементов нет')


