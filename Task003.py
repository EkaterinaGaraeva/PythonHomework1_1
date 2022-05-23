# 3. Напишите программу, смысл которой вот в чем. 
# Программа загадывает вам число из ограниченного диапазона. 
# Ваша цель — отгадать это за log(количество вариантов) попыток. 
# Подсказками компьютера могут служить слова «больше» или «меньше»

import random

def guess_number(log, min, max):
    number = random.randint(min, max)
    print(f"Угадайте число от {min} до {max} за {log} попыток")
    for i in range(log):
        print(f"Попытка № {i + 1}, введите число")
        number1 = input()
        while ((number1.isnumeric() != True) or (int(number1) < min) or (int(number1) > max)):
            print(f"Введенные данные либо не являются целым числом, либо выходят за диапазон угадываемых чисел")
            print(f"Попытка № {i + 1}, введите число")
            number1 = input()
        number1 = int(number1)
        if number1 > number:
            print(f"{number1} больше загаданного числа")
        elif number1 < number:
            print(f"{number1} меньше загаданного числа")
        else:
            print(f"Вы угадали!")
            break
    print(f"Загаданное число {number}")

log = 10 # количество попыток
min = 1 # минимальное число, включительно
max = 99 # максимальное число, включительно
guess_number(log, min, max)
