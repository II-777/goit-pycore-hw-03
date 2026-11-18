from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """Повертає кількість днів від сьогодні до заданої дати.

    Дата має бути рядком у форматі 'РРРР-ММ-ДД'. Час (години, хвилини,
    секунди) у розрахунку не враховується. Якщо задана дата пізніша за
    поточну, результат додатний; якщо раніша — від'ємний. Для рядка
    в неправильному форматі повертає None.
    """
    try:
        given_date = datetime.strptime(date.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None

    today = datetime.today().date()
    return (given_date - today).days


if __name__ == "__main__":
    print(get_days_from_today("2026-10-09")) # дата з минулого (результат від'ємне число)
    print(get_days_from_today("2026-11-28")) # дата з майбутнього (результат позитивне число)
    print(get_days_from_today("не дата"))    # не валідний інпут (результат None)
