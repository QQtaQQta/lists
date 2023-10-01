import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("список случайных чисел:", numbers)
print("повторяющиеся элементы: ")
for number in numbers:
        if numbers.count(number) > 1:
            print(number)