def square(number):
    if number <= 0 or number > 64: raise ValueError('square must be between 1 and 64')
    return pow(2, number - 1)


def total():
    sum = 0
    for i in range(1, 65):
        print(i, square(i))
        sum += square(i)
    return sum
