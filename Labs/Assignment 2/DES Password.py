EXPANSION_TABLE = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,27,3,9,19,13,30,6,22,11,4,25]

def apply_Expansion(expansion_table,bits32):
	""" This will take expansion table and 32-bit binary string as input and output a 48-bit binary stirng"""
	bits48 = ""
	for index in expansion_table:
		bits48 += bits32[index-1]
	return bits48
bits32 = '01100101001000001101010001001010'

out_bits48 = apply_Expansion(EXPANSION_TABLE,bits32)
print(out_bits48)
bits32='00110101111101010010101111011101'
out_bits48 = apply_Expansion(EXPANSION_TABLE,bits32)
print(out_bits48)

# 011110100001010101010101011110100001010101010101