def bubble(array, index):#сортировка пузырьком
    if index % 2 == 0:
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] > array[j+1]:
                    new = array[j]
                    array[j], array[j+1] = array[j+1], new
    else:
        for i in range(len(array)):
            for j in range(len(array)-i-1):
                if array[j] < array[j+1]:
                    new = array[j]
                    array[j], array[j+1] = array[j+1], new
    return array
def sortarray(n):
    arrays = []
    length = [i for i in range(1, 101)]#массив из различных длин для массивов 
    random.shuffle(length)
    for _ in range(n):#создание n массивов в массиве
        arrays.append([])
    for i in range(len(arrays)):#заполнение n массивов в массиве
        for j in range(length[i]):
            arrays[i].append(random.randint(1, 100))
    for i in range(len(arrays)):#цикл для вызова функции bubble
        arrays[i] = bubble(arrays[i], i)
    return(arrays)
import random            
print('Введите количество массивов')
sortarray(int(input()))
