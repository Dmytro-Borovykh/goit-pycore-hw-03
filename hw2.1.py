import random


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
