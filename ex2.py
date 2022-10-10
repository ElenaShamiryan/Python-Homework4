num = int(input('Введите число: '))


def multipliers(num):
    list = []
    n = 2
    while n <= num:
        if num % n == 0:
            list.append(n)
            num = num/n
        else:
            n = n+1
    return list


multipliers = multipliers(num)
print(f'Простые множители числа {num}: {multipliers}')
