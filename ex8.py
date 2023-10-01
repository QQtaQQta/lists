a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print ("список 1: ", a)
print ("список 2: ",b)
common_elements = []

for element in a:
        if element in a and element in b:
            common_elements.append(element)
            
print("список, который состоит из элементов, общих для этих двух списков: ", common_elements)