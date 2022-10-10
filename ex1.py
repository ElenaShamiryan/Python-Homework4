# from math import pi

# d =  int(input("Введите до какой по счету цифры после запятой будет точность числа Пи: "))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


def find_pi(d: float):
    pi, a, b = 3, 1, 2
    while abs(pi - (pi + a * 4 / (b**3 + 3 * b**2 + 2 * b))) > 10**(-d):
        pi = pi + a*4 / (b**3 + 3 * b**2 + 2 * b)
        a = -1 * a
        b = b + 2
    return round((pi + (pi + a*4 / (b**3 + 3 * b**2 + 2*b))) / 2, d)


value = input('Введите точность вычисления d от 0.1 и меньше: ')
d = len(str(value).split('.')[1])
pi = find_pi(d)
print(f'{pi = }')

