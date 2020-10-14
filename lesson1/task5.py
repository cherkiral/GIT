viruchka = int(input("Введите прибыль \n>"))
izderzka = int(input("Введите издержку \n>"))
pribil = int(viruchka - izderzka)
if viruchka > izderzka:
    print ("Работаем в прибыль")
    print(f"Рентабельность выручки равна: {pribil / viruchka}")
    people = int(input("Введите количество сотрудников \n>"))
    print(f"Прибыль в расчете на сотрудника равна {pribil / people}")

elif viruchka == izderzka:
    print ("Мы на грани")
else :
    print ("Работаем в убыток")
