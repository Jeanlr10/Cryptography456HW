def text_to_binary_block(plain_text: str) -> str:
    """
    Converts plain text to a 64-bit binary block using ASCII indices.
    Each character is represented by an 8-bit binary, with the MSB being 0.
    """
    # Convert each character in plain_text to its ASCII value and then to a binary string
    binary_block = ''.join([f"{ord(c):07b}" for c in plain_text])
    
    # Add leading 0 to make each character represented by 8-bit binary
    binary_block_with_msb = ''.join(['0' + binary_block[i:i+7] for i in range(0, len(binary_block), 7)])
    
    # Ensure the block is exactly 64 bits (may need padding or trimming)
    if len(binary_block_with_msb) > 64:
        binary_block_with_msb = binary_block_with_msb[:64]  # Trim to 64 bits if longer
    elif len(binary_block_with_msb) < 64:
        binary_block_with_msb = binary_block_with_msb.ljust(64, '0')  # Pad with zeros if shorter
    
    return binary_block_with_msb


def apply_initial_permutation(binary_block: str, permutation_map: list) -> str:
    """
    Applies an initial permutation to the binary block using a given permutation map.
    """
    # Ensure the binary block is 64 bits
    if len(binary_block) != 64:
        raise ValueError("Binary block must be 64 bits.")
    
    # Apply permutation
    permuted_block = ''.join([binary_block[i - 1] for i in permutation_map])
    
    return permuted_block


# Example usage:
plain_text = "maximize"  # Replace with your plain text

# Convert text to a 64-bit binary block
binary_block = text_to_binary_block(plain_text)
print(f"64-bit binary block: {binary_block}")

# Example permutation map (this should be replaced with your actual map)
permutation_map = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 
                   62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 
                   57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 
                   61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

# Apply the initial permutation
permuted_block = apply_initial_permutation(binary_block, permutation_map)
print(f"Permuted binary block: {permuted_block}")
