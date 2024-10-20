def permutation_operation(input_block, permutation_map):
    """Permute a 32-bit block using the given permutation map."""
    return "".join(input_block[i] for i in permutation_map)

# Output block from Question 4 
s_box_output = "00101110011011101101001110100010" 

# Example permutation map (specific to DES)
permutation_map = [
    15,  6, 19, 20, 28, 11, 27, 16, 
     0, 14, 22, 25,  4, 17, 31,  9, 
     1,  7, 23, 13, 31, 26,  2,  8, 
    18, 13, 29,  5, 21, 10,  3, 24
]

# Perform the permutation operation on the S-Box output
permuted_block = permutation_operation(s_box_output, permutation_map)
print(f"32-bit Block after Permutation Operation: {permuted_block}")
