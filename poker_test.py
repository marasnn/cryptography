from utils.bit_random_generator import generate_random_bits


def fips_140_poker_test(binary_sequence: str) -> bool:
    if len(binary_sequence) != 20000:
        raise ValueError("The binary sequence must be at least 20,000 bits long")
    
    Y = 20_000
    m = 4
    k = 5_000

    chunks = [binary_sequence[i:i+4] for i in range(0, Y, m)]

    frequencies = {}
    for chunk in chunks:
        if chunk not in frequencies:
            frequencies[chunk] = 0
        frequencies[chunk] += 1

    x = (16/5000) * sum(f**2 for f in frequencies.values()) - k

    print(f"X: {x}")
    return 1.03 < x < 57.4


if __name__ == "__main__":
    input_binary_sequence = generate_random_bits(20_000)
    print(fips_140_poker_test(input_binary_sequence))
