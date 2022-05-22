# 2. Есть такая вещь - палиндром. Это когда слово читается 
# с обеих сторон одинаково. Например, слово "шалаш". 
# Также есть числовой палиндром. Если при обратном чтении числа 
# (124 - 421) не получается то же самое, то они складываются (124+421) 
# и проверяются вновь. Попробуйте написать функцию (или просто программу, 
# но лучше все же функцию), находящую числовой палиндром.

def find_palindrome(number):
    number_palindrome = 0
    temp = number
    while int(temp % 10) > 0:
        number_palindrome *= 10
        number_palindrome = number_palindrome + int(temp % 10)
        temp /= 10
    # print(number_palindrome)
    if number == number_palindrome:
        print(f"Число {number} палиндром")
    else:
        print(f"Число {number} не палиндром")
        print(f"{number} + {number_palindrome} = {number + number_palindrome}")
        find_palindrome(number + number_palindrome)

find_palindrome(124)
