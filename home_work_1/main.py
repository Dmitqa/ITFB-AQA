"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers: int) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return list(map(lambda num: num ** 2, numbers))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(cur_num: int) -> bool:
    """
    функция, которая на вход принимает одно число
    и возвращает True / False.
    """
    if cur_num <= 1:
        return False
    elif cur_num == 2:
        return True
    elif cur_num % 2 == 0:
        return False
    for el in range(3, int(cur_num ** 0.5) + 1, 2):
        if cur_num % el == 0:
            return False
    return True


def filter_numbers(num_list: list[int], filter_type: str) -> list[int] | None:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(lambda el: el % 2, num_list))
    elif filter_type == EVEN:
        return list(filter(lambda el: not el % 2, num_list))
    elif filter_type == PRIME:
        return list(filter(is_prime, num_list))
