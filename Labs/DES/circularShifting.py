def circular_left_shift(block):
    new_block = ""
    for i in range(0, 4):
        new_block += block[i*7+1:(i+1)*7] + block[i*7]
        print(new_block)
    return new_block
#def circular_right_shift(block):
#    new_block = ""
#    for i in range(0, 4):
#        new_block += block[i*7+1:(i+1)*7] + block[i*7]
#    return new_block
print(circular_left_shift('1111'))