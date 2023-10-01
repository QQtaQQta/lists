import random

my_list = [random.randint(1, 100) for _ in range(10)]
print("cписок: ", my_list)

x = int(input("Введите число: "))

if x in my_list:
    index = my_list.index(x)
    print(f"число {x} найдено в списке под номером {index}")
else:
    print("-1")
    
""" тут у меня не совсем рандомные числа в списке, а только от 1 до 100, но можено импортировать sys и сделать как
import sys

my_list = [random.randint(sys.minsize, sys.maxsize) for _ in range(10)]
и вот тогда уже реально все рандомные целые будут, но мне кажется это какой-то чересчур большой диапазон для такой задачи 