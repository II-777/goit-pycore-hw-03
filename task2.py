import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Повертає відсортований список унікальних випадкових чисел.

    min — найменше можливе число (не менше 1).
    max — найбільше можливе число (не більше 1000).
    quantity — скільки різних чисел вибрати в діапазоні від min до max
    включно. Якщо параметри цим обмеженням не відповідають, повертає
    порожній список.
    """
    try:
        available = max - min + 1
        if min < 1 or max > 1000 or quantity < 1 or quantity > available:
            return []
        numbers = random.sample(range(min, max + 1), quantity)
    except (TypeError, ValueError):
        return []

    return sorted(numbers)


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
