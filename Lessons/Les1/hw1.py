from my_module import try_input_number

def work(hours, salary, extra):
    """

    :param hours:
    :param salary:
    :param extra:
    :return: hours * salary + extra
    """
    return hours * salary + extra

hours = try_input_number("Input hours")
salary = try_input_number("input salary per hour")
extra = try_input_number("Input extra payment")
print(work(hours, salary, extra))