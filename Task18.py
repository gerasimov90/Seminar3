# Задача 18: Требуется найти в массиве A[1..N] самый 
# близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В 
# последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
some_list = [int(input('Введите элемент списка: ')) 
             for _ in range(int(input('Введите количество элементов в списке: ')))]
x = int(input('Введите значение элемента для поиска: '))
b=[abs(some_list[i]-x) for i in range(len(some_list))]
print(some_list[b.index(min(b))])