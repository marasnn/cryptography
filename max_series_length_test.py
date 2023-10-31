from utils.bit_random_generator import generate_random_bits


def fips_140_max_series_length_test(binary_sequence: str) -> bool:
    MAX_SERIES_LENGTH = 36
    
    if not binary_sequence:
        return False
    
    ones_count = 0
    zeros_count = 0
    max_ones_count = 0
    max_zeros_count = 0
    
    for bit in binary_sequence:
        if bit == '1':
            ones_count += 1
            zeros_count = 0
            if ones_count > max_ones_count:
                max_ones_count = ones_count
        elif bit == '0':
            zeros_count += 1
            ones_count = 0
            if zeros_count > max_zeros_count:
                max_zeros_count = zeros_count
    
    print(f"Max ones count: {max_ones_count}, Max zeros count: {max_zeros_count}")
    if max_ones_count >= MAX_SERIES_LENGTH or max_zeros_count >= MAX_SERIES_LENGTH:
        return False
    return True

if __name__ == "__main__":
    input_binary_sequence = generate_random_bits(20_000)
    print(fips_140_max_series_length_test(input_binary_sequence))
