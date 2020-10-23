while True:
    try:
            x = float(input("Input first number\n"))
            y = float(input("Input second number\n"))
            break
    except ValueError:
        print('Only numbers in input')



def my_func(x, y):
    return x**y
print(my_func(x, y))


def my_func_cycle(x,y):
    mult = 1
    count = 0

    while count < abs(y):
        mult = x * mult
        count += 1
    result = 1 / mult
    return result
print(my_func_cycle(x, y))