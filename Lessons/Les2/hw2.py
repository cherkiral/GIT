list = []
choise = input ("Напишите + если, хотите добавить элемент в список и -, если не хотите добавлять\n>")
if choise == "+" :
    choice1 = "+"
    while choice1 == "+" :
        piece = input("Введите элемент списка\n>")
        list.append(piece)
        choice1 = input("Напишите +, если хотите добавить еще один элемент и -, если не хотите\n>")

elif choise == "-":
    print("Ничего не добавлено\n")


i = 0
for j in range(0, len(list) // 2 ):
    list[i], list[i+1] = list[i+1], list[i]
    i += 2

print(f"Измененный список: {list}")







