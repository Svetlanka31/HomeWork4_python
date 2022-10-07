#  2.Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
list1 = [random.randint(1,21) for i in range(5)]
print(list1)
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i) 
print(list2)