import random
from datetime import date, timedelta


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
