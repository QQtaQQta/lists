import random

numbers = [random.randint(1, 100) for _ in range(10)]

max_number = max(numbers)

print("список случайных чисел:" , numbers)
print("наибольший элемент списка:" , max_number)