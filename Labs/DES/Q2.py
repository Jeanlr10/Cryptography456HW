def key_to_binary_block(key: str) -> str:
    """
    Converts the key to a 64-bit binary block using ASCII indices.
    Each character is represented by a 7-bit ASCII binary followed by a 0 (verification bit).
    """
    # Convert each character in the key to its ASCII value and then to a binary string
    binary_block = ''.join([f"{ord(c):07b}" for c in key])
    
    # Add a verification bit (0) to each 7-bit binary number
    binary_block_with_verification = ''.join([binary_block[i:i+7] + '0' for i in range(0, len(binary_block), 7)])
    
    # Ensure the block is exactly 64 bits (may need padding or trimming)
    if len(binary_block_with_verification) > 64:
        binary_block_with_verification = binary_block_with_verification[:64]  # Trim to 64 bits if longer
    elif len(binary_block_with_verification) < 64:
        binary_block_with_verification = binary_block_with_verification.ljust(64, '0')  # Pad with zeros if shorter
    
    return binary_block_with_verification


def left_shift(binary_half: str, shifts: int = 1) -> str:
    """
    Performs a left shift on a given binary string (half of the key) by a specified number of shifts.
    """
    return binary_half[shifts:] + binary_half[:shifts]


def apply_pc2(binary_block: str, pc2_map: list) -> str:
    """
    Applies the permuted choice 2 (PC-2) operation using the given permutation map.
    """
    return ''.join([binary_block[i - 1] for i in pc2_map])

#Input Key here
key = "fabulous"



# Step 1: Convert the key to a 64-bit binary block
binary_key = key_to_binary_block(key)
print(f"64-bit binary key block: {binary_key}")

# Split into two halves (32-bit each for DES)
left_half = binary_key[:32]
right_half = binary_key[32:]

# Step 2: Shift each half by 1 bit to the left
shifted_left_half = left_shift(left_half, 1)
shifted_right_half = left_shift(right_half, 1)

# Combine the shifted halves back
shifted_key = shifted_left_half + shifted_right_half
print(f"Shifted key (after left shift): {shifted_key}")

# Example PC-2 permutation map (Replace with actual PC-2 map for DES)
pc2_map = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 
           26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 
           51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# Step 3: Apply Permuted Choice 2 (PC-2) to the shifted key
pc2_key = apply_pc2(shifted_key, pc2_map)
print(f"Key after PC-2 operation: {pc2_key}")
