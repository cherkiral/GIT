from my_module import try_input_number

def fact(factorial_number):
    """

    :param factorial_number: A number that we will take the factorial of
    :return: factorial of a number
    """
    factorial = 1

    for i in range(2, factorial_number + 1):
        factorial *= i
    yield factorial

for el in fact(try_input_number("")):
    print(el)