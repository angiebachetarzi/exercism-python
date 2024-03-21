from functools import reduce
def is_valid(isbn):
    isbn_trimmed = isbn.replace('-', '')
    #string must be equal to 10
    if len(isbn_trimmed) != 10:
        return False
    #contains letter (not at the end)
    if not isbn_trimmed[:-1].isnumeric():
        return False
    #letter can only be X
    if isbn_trimmed[-1].isalpha() and isbn_trimmed[-1] != 'X':
         return False
    if isbn_trimmed[-1].isalpha():
        digits = [int(d) for d in isbn_trimmed[:-1]]
    else:
        digits = [int(d) for d in isbn_trimmed]
    weights = list(range(10, 0, -1))
    reduce_res = reduce(weighted_product, zip(digits, weights), 0)
    if isbn_trimmed[-1].isalpha():
        reduce_res += 10
    return reduce_res % 11 == 0

def weighted_product(acc, digit_weight):
        digit, weight = digit_weight
        return acc + digit * weight
