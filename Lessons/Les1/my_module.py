def list_creation():
    """

    :return: Returns a list of int numbers
    """
    while True:
        try:
            user_list = list(map(int, input('Input numbers separated by space \n>').split()))
            break
        except ValueError:
            print('Incorrect input')
    return user_list

def list_multiply(elem, elem1):
    """

    :param elem: Previous element
    :param elem1: Next element
    :return: Multiplied elements
    """
    return elem * elem1

def try_input_number(some_text):
    """

    :param some_text: A text to customise input
    :return: Returns a number
    """
    print(some_text)
    while True:
        try:
            user_number = int(input("Enter a number\n>"))
            break
        except ValueError:
            print('Incorrect input')
    return user_number