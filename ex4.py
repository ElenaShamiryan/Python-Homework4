import random


k = int(input('Введите степень: '))


def equation(k):
    list = []
    for i in range(k, -1, -1):
        d = random.randint(0, 100)
        if i == 0:
            list.append(f'{d}')
        elif i == 1:
            list.append(f'{d}x')
            list.append('+')
        else:
            list.append(f'{d}x^{i}')
            list.append('+')
    list.append('= 0')
    a = " ".join(map(str, list))
    return (a)

new_eq = equation(k)
with open('file.txt', 'w', encoding='utf8') as file:
    file.write(new_eq)