from utils.bit_random_generator import generate_random_bits


def fips_140_monobit_test(binary_sequence: str) -> bool:
    
    LOWER_BOUND = 9654
    UPPER_BOUND = 10346
    
    ones_count = binary_sequence.count('1')
    zeros_count = binary_sequence.count('0')
    
    print(f"Ones count: {ones_count}, Zeros count: {zeros_count}")
    if LOWER_BOUND <= ones_count <= UPPER_BOUND and LOWER_BOUND <= zeros_count <= UPPER_BOUND:
        return True
    return False

    
if __name__ == "__main__":
    input_binary_sequence = generate_random_bits(20_000)
    print(fips_140_monobit_test(input_binary_sequence))
