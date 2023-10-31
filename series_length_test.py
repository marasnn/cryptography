from utils.bit_random_generator import generate_random_bits


def fips_140_series_length_test(binary_sequence: str) -> bool:

    counts = {length: 0 for length in range(1, 7)}

    current_bit = binary_sequence[0]
    current_length = 1
    for bit in binary_sequence[1:]:
        if bit == current_bit:
            current_length += 1
        else:
            counts[min(current_length, 6)] += 1
            current_bit = bit
            current_length = 1

    print("Counts:", dict(sorted(counts.items())))
    return (2267 <= counts[1] <= 2733 and
            1079 <= counts[2] <= 1421 and
            502 <= counts[3] <= 748 and
            223 <= counts[4] <= 402 and
            90 <= counts[5] <= 223 and
            90 <= counts[6] <= 223)


if __name__ == "__main__":
    input_binary_sequence = generate_random_bits(20_000)
    print(fips_140_series_length_test(input_binary_sequence))
