import random


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
