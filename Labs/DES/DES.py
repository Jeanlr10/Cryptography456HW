def char_to_ascii_binary(char, parity):
    # Convert the character to 7-bit ASCII and add a parity bit (0)
    ascii_val = ord(char)
    if parity:
        binary_val = f'{ascii_val:07b}0' # 7 bits of ASCII + 1 parity bit (0)
    else:
        binary_val = f'0{ascii_val:07b}'  
    return binary_val

def text_to_binary_block(text, parity=True):
    # Convert the entire text to a 64-bit binary block
    binary_block = ''.join([char_to_ascii_binary(c, parity) for c in text])
    return binary_block

def print_table(arr, row_nums):
    for i in range(0, len(arr), row_nums):
        # Print a slice of the array from index i to i+row_nums
        print(arr[i:i+row_nums])

IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# PC-1 table (56-bit permutation)
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# PC-2 table (48-bit permutation)
PC2 = [
    14, 17, 11, 24, 1,  5, 
    3,  28, 15, 6,  21, 10, 
    23, 19, 12, 4,  26, 8, 
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 
    30, 40, 51, 45, 33, 48, 
    44, 49, 39, 56, 34, 53, 
    46, 42, 50, 36, 29, 32
]

# Expansion table (32 to 48 bits)
expansion_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

def expand_block(block):
    expanded_block = ''.join([block[i - 1] for i in expansion_table])
    return expanded_block

# Circular left shift (1-bit)
def circular_left_shift(block):
    new_block = ""
    for i in range(0, 4):
        new_block += block[i*7+1:(i+1)*7] + block[i*7]
    return new_block

def apply_permutation(block, table):
    # Apply the permutation based on the given table
    return ''.join([block[i - 1] for i in table])

def generate_subkey(text):
    print("Generate Subkey For Round 1")
    print("Step 1: Convert the key (text) to 64-bit binary block")
    binary_block = text_to_binary_block(text)
    print_table(binary_block, 8)

    print("Step 2: Apply PC-1 to get a 56-bit block")
    pc1_result = apply_permutation(binary_block, PC1)
    print_table(pc1_result, 7)

    print("Step 3: Split into two halves (C0, D0)")
    C0, D0 = pc1_result[:28], pc1_result[28:]
    print("C0 (left half):")
    print_table(C0, 7)
    print("D0 (right half):")
    print_table(D0, 7)

    print("Step 4: Perform 1-bit circular left shift on both C0 and D0")
    C1 = circular_left_shift(C0, 1)
    D1 = circular_left_shift(D0, 1)
    print("C1 (after 1-bit shift):")
    print_table(C1, 7)
    print("D1 (after 1-bit shift):")
    print_table(D1, 7)

    print("Step 5: Apply PC-2 to get a 48-bit subkey")
    combined_C1_D1 = C1 + D1
    subkey = apply_permutation(combined_C1_D1, PC2)
    print_table(subkey, 6)

    return subkey

def generate_IP_and_split_and_expand(plaintext):
    print("Generate IP, Split, and Expand")
    print("Step 1: Convert plaintext to binary block (64 bits) and then IP")
    bin_block = text_to_binary_block(plaintext, parity=False)
    print_table(bin_block, 8)
    binary_block = apply_permutation(bin_block, IP)
    
    print("64-bit block after initial permutation (IP):")
    print_table(binary_block, 8)

    print("Step 2: Split the block into two halves (L0, R0)")
    L0 = ""
    R0 = ""
    # Calculate the total number of rows and columns
    rows = 8  # We have 2 rows
    cols = 8  # We can assume there are 8 columns in this example

    # Loop through each row
    for row in range(rows):
        for col in range(cols):
            index = row * cols + col  # Calculate the index in the binary string
            if col < cols // 2:  # If it's in the left half
                L0 += binary_block[index]  # Append to L0
            else:  # If it's in the right half
                R0 += binary_block[index]  # Append to R0

    print("L0 (left half):")
    print_table(L0, 4)
    print("R0 (right half):")
    print_table(R0, 4)

    print("Step 3: Expand R0 to 48 bits")
    expanded_R0 = expand_block(R0)
    print_table(expanded_R0, 6)

    return expanded_R0, L0, R0

S_BOXES = {
    "00": {
        "0000": "0010",
        "0001": "1100",
        "0010": "0100",
        "0011": "0001",
        "0100": "0111",
        "0101": "1010",
        "0110": "1011",
        "0111": "0110",
        "1000": "1000",
        "1001": "0101",
        "1010": "0011",
        "1011": "1111",
        "1100": "1101",
        "1101": "0000",
        "1110": "1110",
        "1111": "1001"
    },
    "01": {
        "0000": "1110",
        "0001": "1011",
        "0010": "0010",
        "0011": "1100",
        "0100": "0100",
        "0101": "0111",
        "0110": "1101",
        "0111": "0001",
        "1000": "0101",
        "1001": "0000",
        "1010": "1111",
        "1011": "1010",
        "1100": "0011",
        "1101": "1001",
        "1110": "1000",
        "1111": "0110"
    },
    "10": {
        "0000": "0100",
        "0001": "0010",
        "0010": "0001",
        "0011": "1011",
        "0100": "1010",
        "0101": "1101",
        "0110": "0111",
        "0111": "1000",
        "1000": "1111",
        "1001": "1001",
        "1010": "1100",
        "1011": "0101",
        "1100": "0110",
        "1101": "0011",
        "1110": "0000",
        "1111": "1110"
    },
    "11": {
        "0000": "1011",
        "0001": "1000",
        "0010": "1100",
        "0011": "0111",
        "0100": "0001",
        "0101": "1110",
        "0110": "0010",
        "0111": "1101",
        "1000": "0110",
        "1001": "1111",
        "1010": "0000",
        "1011": "1001",
        "1100": "1010",
        "1101": "0100",
        "1110": "0101",
        "1111": "0011"
    }
}

# Final Permutation Table
P_TABLE = [
    19, 2, 1, 16,
    13, 8, 15, 7,
    30, 24, 23, 20,
    6, 14, 26, 21,
    2, 32, 5, 29,
    11, 27, 18, 12,
    4, 3, 31, 28,
    25, 9, 10, 17
]

def xor_s_box_permutation_xor2(expand_block, subkey):
    print("XOR1, S-Box, permutation, and then XOR2")
    print("Step 1: XOR the expanded block with the subkey")
    xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(expand_block, subkey))
    print_table(xor_result, 6)

    print("Step 2: S-Box substitution")
    s_box_output = ""
    for i in range(0, 48, 6):  # Process the XOR result in chunks of 6 bits
        block = xor_result[i:i+6]
        row = int(block[0] + block[5], 2)  # First and last bits form the row (convert to int)
        col = int(block[1:5], 2)  # Middle four bits form the column (convert to int)
        s_value = S_BOXES[f'{row:02b}'][f'{col:04b}']  # Get the S-Box value for this chunk
        s_box_output += s_value  # Concatenate the 4-bit output from the S-Box

    print_table(s_box_output, 4)

    print("Step 3: Apply final permutation (P) on the S-Box output")
    final_permuted_block = apply_permutation(s_box_output, P_TABLE)
    print_table(final_permuted_block, 4)

    # Return the result
    return final_permuted_block


text = 'maximize'
key = 'fabulous'
expanded_R0, L0, R0 = generate_IP_and_split_and_expand(text)
pc2_block = generate_subkey(key)
final_permuted_block = xor_s_box_permutation_xor2(expanded_R0, pc2_block)