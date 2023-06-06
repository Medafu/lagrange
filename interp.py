dict = {1: 15, 2: 17, 3: 7, 4: 21}
x = 2.5

def lagrange_interp(dict, x):
    result = 0

    for i in dict.keys():
        result += dict[i] * calc_division(x, dict, i)
    return result

def calc_division(x, dict, curr):
    result_dividend = 1
    result_divisor = 1
    for i in dict.keys():
        if i == curr:
            continue

        result_dividend *= x - i
        result_divisor *= curr - i
    return result_dividend / result_divisor

print(lagrange_interp(dict, x))
