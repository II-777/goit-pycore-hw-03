import re


def normalize_phone(phone_number: str) -> str:
    """Нормалізує телефон до вигляду, придатного для SMS-розсилки.

    Залишає лише цифри та '+' на початку. Якщо міжнародного коду немає,
    додає '+38'. Номер, який уже починається з '380', отримує лише '+'.
    """
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    if cleaned.startswith("+"):
        digits = re.sub(r"\D", "", cleaned)
        return f"+{digits}"

    if cleaned.startswith("380"):
        return f"+{cleaned}"

    return f"+38{cleaned}"


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
