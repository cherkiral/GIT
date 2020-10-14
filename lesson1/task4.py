num = int(input("Введите число \n>"))
max = num % 10
while num > 0:
    i = num % 10
    num = int(num / 10)
    if i > max:
        max = i
print(f"Наибольшая цифра в числе {max}")
