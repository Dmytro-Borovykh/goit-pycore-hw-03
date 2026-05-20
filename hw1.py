import random
from datetime import datetime
import re
from datetime import date, timedelta

# ----------------- EX1 -----------------


def get_days_from_today(date: str) -> int:
    try:
        # Перетворення рядка у дату
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Поточна дата
        today = datetime.today().date()
        # Повернення різницi між датами
        return (today - given_date).days

    except ValueError:
        return "Incorrect date format. Use YYYY-MM-DD"


print(get_days_from_today("2026-01-01"))

# Тести
assert isinstance(get_days_from_today("2024-01-01"), int)
assert get_days_from_today("2021-10-09") > 0
assert get_days_from_today("2030-10-09") < 0
assert get_days_from_today(
    "2026.01.01") == "Incorrect date format. Use YYYY-MM-DD"


# ----------------- EX2 _ v1 -----------------
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:

    if isinstance(min, int) and \
            isinstance(max, int) and \
            isinstance(quantity, int) and \
            1000 > min >= 1 and \
            1 < max < 1000 and \
            min < max and \
            quantity > 0 and \
            quantity <= (max - min + 1):

        numbers = random.sample(range(min, max + 1), quantity)

    else:
        print('pls check your condition')
        return []

    return sorted(numbers)


# Tests
result = get_numbers_ticket(1, 49, 6)
assert isinstance(result, list)
assert len(result) == 6
assert result == sorted(result)
assert min(result) >= 1
assert max(result) <= 49


assert get_numbers_ticket(0, 49, 6) == []
assert get_numbers_ticket(1, 49, 0) == []
assert get_numbers_ticket(1, 0, 49) == []
assert get_numbers_ticket(2, 1000, 49) == []


# ----------------- EX2 _ v2 -----------------

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if checkCondition(min, max, quantity):
        return sorted(random.sample(range(min, max + 1), quantity))
    else:
        return []


def checkCondition(min: int, max: int, quantity: int):
    if not isinstance(min, int):
        return False

    if not isinstance(max, int):
        return False

    if not isinstance(quantity, int):
        return False

    if not (1000 > min >= 1):
        return False

    if not (1 < max < 1000):
        return False

    if not (min < max):
        return False

    if not (quantity > 0):
        return False

    if not (quantity <= (max - min + 1)):
        return False
    else:
        return True


print('ex2')
print(get_numbers_ticket(1, 6, 6))


# ----------------- EX3 -----------------

def normalize_phone(phone_number: str) -> str:

    cleaned = re.sub(r'[^\d+]', '', phone_number)

    if cleaned.startswith('+38'):
        return cleaned
    elif cleaned.startswith('38'):
        return '+' + cleaned
    else:
        return '+38' + cleaned


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


# ----------------- EX4 -----------------

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:

    if not isinstance(users, list):
        raise TypeError(f"should be list")

    today = date.today()
    upcoming = []

    for user in users:
        birthday = date.fromisoformat(user["birthday"].replace(".", "-"))

        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        delta = (birthday_this_year - today).days
        if not (0 <= delta <= 6):
            continue

        congratulation_date = birthday_this_year
        if congratulation_date.weekday() == 5:   # суббота
            congratulation_date += timedelta(days=2)
        elif congratulation_date.weekday() == 6:  # воскресенье
            congratulation_date += timedelta(days=1)

        upcoming.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
        })

    return upcoming


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "John Doe Junior", "birthday": "2026.05.23"},
    {"name": "Jane Smith Junior", "birthday": "2026.05.22"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
