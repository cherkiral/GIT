def division():
    while True:
        try:
            x = float(input("Input first number\n"))
            y = float(input("Input second number\n"))
            break
        except ValueError:
            print('Only numbers in input')

    if y != 0:
        return x / y

    else:
        return "division by 0"

print(division())
