def validator(validator_pseudo_function, exception_message):
    def wrapper(func):
        def execute(arg1, arg2, operator):
            if operator == '>':
                return arg1 > arg2
            elif operator == '<':
                return arg1 < arg2
            elif operator == 'in':
                return arg1 in arg2
            elif operator == 'startswith':
                return arg1[:len(arg2)] == arg2
            else:
                raise ValueError


        def wrapped_function(arg):
            arg2, operator = validator_pseudo_function
            if execute(arg, arg2, operator):
                return func(arg)
            else:
                print(exception_message)


        return wrapped_function
    return wrapper


def greater_than(arg):
    return (arg, '>')


def less_than(arg):
    return (arg, '<')


def arg_in(arg):
    return (arg, 'in')


def starts_with(arg):
    return (f'{arg}', 'startswith')


@validator(less_than(5), 'exception_for_less')
@validator(greater_than(3), 'exception_for_greater')
def print_int(integer: int):
    print(integer)


@validator(arg_in([1, 3, 5, 7]), 'not_in_first_four')
def print_if_in_first_four_prime(integer):
    print(integer)


@validator(starts_with('desktop:'), 'wrong')
def print_if_cmd_string(string):
    print(string)


if __name__=='__main__':
    print_int(6)
    print_int(5)
    print_int(4)
    print_int(3)
    print_int(2)

    print_if_in_first_four_prime(1)
    print_if_in_first_four_prime(2)

    print_if_cmd_string('desktop:1')
    print_if_cmd_string('des:1')
