def my_func(*args):

    if args[0] >= args[1]:
        if args[0] >= args[2] and args[1] >= args[2]:
            return args[0] + args[1]
        elif args[0] <= args[2]:
            return args[2] + args[0]
        else:
            return args[0] + args[2]
    else:
        return args[1] + args[2]


while True:
    try:
            a = float(input("Input first number\n"))
            b = float(input("Input second number\n"))
            c = float(input("Input third number\n"))
            break
    except ValueError:
        print('Only numbers in input')


print(my_func(a, b, c))

