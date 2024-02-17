def steps(number):
    if number <= 0: raise ValueError('Only positive integers are allowed')
    return conjecture(number, 0)

def conjecture(number, steps):
    if number == 1: return steps
    elif number % 2 == 0:
            return conjecture(number//2, steps + 1)
    else:
            return conjecture(number * 3 + 1, steps + 1)
