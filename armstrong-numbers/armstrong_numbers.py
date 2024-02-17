import functools

def is_armstrong_number(number):
    number_string = str(number)
    if len(number_string) == 1: return True
    sum = functools.reduce(lambda a, b: int(a) + pow(int(b), len(number_string)), number_string, 0)
    return sum == number
    
