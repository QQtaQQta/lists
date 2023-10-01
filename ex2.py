my_list = []
for i in range(1, 101):
    if i % 2 == 0:
        my_list.append(i)
        if len(my_list) == 50:
            break

print(my_list)