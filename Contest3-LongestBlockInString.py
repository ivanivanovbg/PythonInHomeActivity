def get_longest_block(inp_str:str)->str:
    longest_block_char = ""
    temp_longest_block = 1
    longest_block = 1
    i = 1
    while i < len(inp_str):
        if inp_str[i] == inp_str[i-1]:
            temp_longest_block += 1
        else:
            if temp_longest_block > longest_block:
                longest_block = temp_longest_block
                longest_block_char = inp_str[i-1]
            temp_longest_block = 1
        i+=1

    if temp_longest_block > longest_block:
        longest_block = temp_longest_block
        longest_block_char = inp_str[i-1]
        
    if longest_block == 1:
        return inp_str[0]
    return longest_block_char*longest_block

input_string = input()
print(get_longest_block(input_string))