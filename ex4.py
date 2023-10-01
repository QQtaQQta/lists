import random

numbers = [random.randint(1, 100) for _ in range(10)]
sum_numbers = sum(numbers)
product_numbers = 1
for number in numbers:
    product_numbers *= number
print("cписок случайных чисел: ", numbers, end=" ")
print("\ncумма чисел в списке: ", sum_numbers)
print("gроизведение чисел в списке: ", product_numbers)

#тут ситуация с рандомностью заполнения списка а же, что и в задании 3, да и в целом далее будет вот так вот