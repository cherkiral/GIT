my_list = input("Введите несколько слов через пробел\n>")
splited = (my_list.split())
count = 0
for i in splited:
    print(f"Слово номер {count+1} : {splited[count][:10]} ")
    count += 1