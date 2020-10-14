a = int(input("Введите результат в первый день \n>"))
b = int(input("Введите максимальны результат спортсмена \n>"))
day = 1
result = a
while day > 0:
    day += 1
    result *= 1.1
    if result <= b:
        print(f"Результат в {day} день равен {round(result, 2)}")
    else :
        print(f"Результат в {day} день равен {round(result, 2)}\n\n")
        print(f"Ответ: на {day} день спортсмен достиг результата — не менее {b} км.")
        break
