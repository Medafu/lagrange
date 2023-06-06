dict = {1: 0.16667, 1.1: 0.15470, 1.2: 0.14137, 1.3: 0.12729, 1.4: 0.11310, 1.5: 0.09938}
y = 0.13438

def lagrange_interp(dict, y):
    result = 0

    for i in dict.keys():
        result += i * calc_division(dict, y, i)
    return result

def calc_division(dict, y, curr):
    result_dividend = 1
    result_divisor = 1
    for i in dict.keys():
        if i == curr:
            continue

        result_dividend *= y - dict[i]
        result_divisor *= dict[curr] - dict[i]
    return result_dividend / result_divisor

print(lagrange_interp(dict, y))
