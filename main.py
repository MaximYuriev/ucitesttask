import random
from functools import reduce


#Ссылка на git: https://github.com/MaximYuriev/ucitesttask

def deco(func): # декоратор, обрабатывающие ошибки при взаимодействии с функциями
    def wrapper(array: list[int]):
        if not isinstance(array, list):
            raise TypeError('Функция работает только со списками!')
        if not array:
            raise TypeError('Список не может быть пустым!')
        return func(array)
    return wrapper

@deco
def list_sum_by_sum(array: list[int]) -> int:
    """
    Вычисляет сумму всех элементов списка с помощью встроенной функции
    :param array: список целых чисел
    :return: сумма чисел, содержащихся в списке
    """
    return sum(array)

@deco
def list_sum_by_reduce(array: list[int]) -> int:
    """
    Вычисляет сумму всех элементов списка с использованием lambda-функции и применением функции reduce
    :param array: список целых чисел
    :return: сумма чисел, содержащихся в списке
    """
    return reduce(lambda x,y: x+y, array)

@deco
def list_avg_by_sum_and_len(array:list[int]) -> float:
    """
    Вычисляет среднее значение списка с помощью встроенных функций sum и len
    :param array: список целых чисел
    :return: среднее значение чисел, содержащихся в списке
    """
    return sum(array)/len(array)

@deco
def list_avg_by_map_reduce(array:list[int]) -> float:
    """
    Вычисляет среднее значение списка с помощью функций map, reduce и lambda
    :param array: список целых чисел
    :return: среднее значение чисел, содержащихся в списке
    """
    n = len(array)
    array_del_len = list(map(lambda x: x/n, array))
    return reduce(lambda x,y: x+y, array_del_len)

@deco
def list_max_by_max(array:list[int]) -> int:
    """
    Находит максимальный элемент в списке, используя функцию max
    :param array: список целых чисел
    :return: максимальный элемент списка
    """
    return max(array)

@deco
def list_max_by_reduce(array:list[int]) -> int:
    """
    Находит максимальный элемент списка, используя функции reduce, lambda
    :param array: список целых чисел
    :return: максимальный элемент списка
    """
    return reduce(lambda x,y: x if x > y else y, array)

@deco
def list_min_by_min(array:list[int]) -> int:
    """
    Находит минимальный элемент списка, используя функцию min
    :param array: список целых чисел
    :return: минимальный элемент списка
    """
    return min(array)

@deco
def list_min_by_reduce(array:list[int]) -> int:
    """
    Находит минимальный элемент списка при помощи reduce и lambda
    :param array: список целых чисел
    :return: минимальный элемент списка
    """
    return reduce(lambda x,y: y if x > y else x, array)

if __name__ == '__main__':
    random_list = [random.randint(1, 100) for _ in range(10)]
    print(f"Сгенерированный список случайных чисел: {random_list}")

    print(f"Сумма чисел списка, посчитанная функцией sum: {list_sum_by_sum(random_list)}")
    print(f"Сумма чисел списка, посчитанная с помощью reduce: {list_sum_by_reduce(random_list)}")

    print(f"Среднее значение списка, полученное с использованием функций sum и len: {list_avg_by_sum_and_len(random_list)}")
    print(f"Среднее значение элементов списка, полученное с помощью map и reduce: {list_avg_by_map_reduce(random_list)}")

    print(f"Максимальный элемент списка, полученный функцией max: {list_max_by_max(random_list)}")
    print(f"Максимальный элемент списка, полученный с помощью reduce: {list_max_by_reduce(random_list)}")

    print(f"Минимальный элемент списка, полученный функцией min: {list_min_by_min(random_list)}")
    print(f"Минимальный элемент списка, полученный функцией reduce: {list_min_by_reduce(random_list)}")