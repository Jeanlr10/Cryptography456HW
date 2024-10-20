def expansion_function(input_block, expansion_map):
    """Expand a 32-bit block into a 48-bit block using the expansion map."""
    expanded_block = "".join(input_block[i] for i in expansion_map)
    return expanded_block

# Input block is the right half (last 32 bits) of the binary block from Question 1
input_block_from_q1 = "" 

# Example expansion map (specific to DES, typically it expands 32 bits to 48 bits)
expansion_map = [31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 
                 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 
                 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 
                 27, 28, 27, 28, 29, 30, 31, 0]

# Perform the expansion function on the input block
expanded_block = expansion_function(input_block_from_q1, expansion_map)
print(f"Expanded 48-bit Block: {expanded_block}")
