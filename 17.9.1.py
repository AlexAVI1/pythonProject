# Запрашиваем числа у пользователя
input_numbers = input('Введите числа через пробел: ')
any_number = int(input('Введите любое число: '))
error = 'В процессе выполнения программы возникла ошибка. Необходимо запустить программу повторно!'

# Определяем цифры в строке
def checking(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False


# Проверка на соответствие ввода данных

if " " not in input_numbers:
    print("\nВ веденных данных отсутствуют пробелы (некорректный ввод). Введите числа через пробел.")
    input_numbers = input('Введите числа через пробел: ')
if not checking(input_numbers):
    print('\nВведены данные не соответствуют числовым данным (некорректный ввод). Введите числа через пробел.\n')
    print(error)

else:
    input_numbers = input_numbers.split()


list_input_numbers = [int(item) for item in input_numbers] # Преобразование введённой последовательности в список


# Сортировка списка
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list_input_numbers = merge_sort(list_input_numbers)

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

# Устанавливается номер позиции элемента, который меньше
# введенного пользователем числа, а следующий за ним больше или равен этому числу.

print(f'Упорядоченный по возрастанию список: {list_input_numbers}')

if not binary_search(list_input_numbers, any_number, 0, len(list_input_numbers)):
    El = min(list_input_numbers, key=lambda x: (abs(x - any_number), x))
    index_list = list_input_numbers.index(El)
    max_ind = index_list + 1
    min_ind = index_list - 1
    if El < any_number:
        print(f'''В списке нет введенного элемента: 
меньший элемент: {El} и его индекс: {index_list}
больший элемент: {list_input_numbers[max_ind]} и его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента:
больший элемент элемент: {El} и его индекс: {list_input_numbers.index(El)}
В списке нет меньшего элемента''')
    elif El > any_number:
        print(f'''В списке нет введенного элемента
больший элемент: {El}  и его индекс: {list_input_numbers.index(El)}
меньший элемент: {list_input_numbers[min_ind]} и его индекс: {min_ind}''')
    elif list_input_numbers.index(El) == 0:
        print(f'Индекс введенного элемента: {list_input_numbers.index(El)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_input_numbers, any_number, 0, len(list_input_numbers))}')
