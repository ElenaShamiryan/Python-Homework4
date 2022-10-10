import random

n = int(input('Введите длину списка: '))
list = []

def first_list(list):
    for i in range(n):
        num = random.randint(1,7)
        list.append(num)
    print(f'Исходный  список: {list}')

first_list(list)

for i in range(len(list)):
    count = 1
    for j in range(len(list)):
        if list[i] == list[j] and i != j:
            count = 0
            break
    if count:
        print(list[i], end=' ')
  

