def convert(number):
    div3 = number % 3 == 0
    div5 = number % 5 == 0
    div7 = number % 7 == 0
    str_res = ''
    if div3:
        str_res += 'Pling'
    if div5:
        str_res += 'Plang'
    if div7:
        str_res += 'Plong'
    if not str_res:
        return str(number)
    return str_res