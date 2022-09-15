#Сортировка бинарными вставками


def insertion_sort(data):
    for i in range(1, len(data)):
        current_element = data[i]
        left = 0
        right = i - 1
        while left <= right: #ищем место вставки
            middle_index = (left + right) // 2
            if current_element < data[middle_index]:
                right = middle_index - 1
            else:
                left = middle_index + 1
        #сдвигаем элементы роассположенные правее места вставки
        j = i-1
        while j >= left:
            data[j+1] = data[j]
            j = j - 1
        data[left] = current_element
    return data

data = [2, 34, 5, 6, 0]
print(insertion_sort(data))



