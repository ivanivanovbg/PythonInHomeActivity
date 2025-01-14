def get_longest_seq(num_array:[str])->int:
    longest_sequence = 1
    temp_longest_sequence = 1
    for i in range(1,len(num_array)):
        if num_array[i] == num_array[i-1]:
            temp_longest_sequence += 1
        else:
            if temp_longest_sequence > longest_sequence:
                longest_sequence = temp_longest_sequence
            temp_longest_sequence = 1
    if temp_longest_sequence > longest_sequence:
        return temp_longest_sequence
    else:
        return longest_sequence

rows = int(input())
input_number = rows*['']
for row in range(rows):
    input_number[row] = input()
print(get_longest_seq(input_number))