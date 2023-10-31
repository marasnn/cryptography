import random


def generate_random_bits(length: int) -> str:
    return ''.join(str(random.choice([0, 1])) for _ in range(length))
