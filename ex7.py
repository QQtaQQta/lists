import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("исходный список: ", numbers) 

max_index = numbers.index(max(numbers))
min_index = numbers.index(min(numbers))

numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]

print("новый список: ", numbers)