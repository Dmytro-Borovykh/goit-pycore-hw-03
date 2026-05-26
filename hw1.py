from datetime import datetime


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
