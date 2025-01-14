def calc_pos_row(i_matrix:[[int]],row_num:int,col_num:int)->int:
    r_sum = 0
    col_num = abs(col_num)
    for j in range(col_num):
        r_sum += i_matrix[row_num-1][j]
    return r_sum
def calc_neg_row(i_matrix:[[int]],row_num:int,col_num:int)->int:
    r_sum = 0
    row_num = abs(row_num)
    col_num = abs(col_num)
    for j in range(col_num-1,max_c_num):
        r_sum += i_matrix[row_num-1][j]
    return r_sum
def calc_pos_col(i_matrix:[[int]],row_num:int,col_num:int)->int:
    r_sum = 0
    row_num = abs(row_num)
    for j in range(row_num-1):
        r_sum += i_matrix[j][col_num-1]
    return r_sum
def calc_neg_col(i_matrix:[[int]],row_num:int,col_num:int)->int:
    r_sum = 0
    row_num = abs(row_num)
    col_num = abs(col_num)
    for j in range(row_num,inp_rows):
        r_sum += i_matrix[j][col_num-1]
    return r_sum
inp_rows = int(input())
matrix = inp_rows*[[]]
for i in range(inp_rows):
    matrix[i] = list(map(int,input().split()))
cpairs = list(map(int,input().split()))
max_sum = -2000001
sums = []
temp_max_sum = 0
max_c_num = len(matrix[0])
for i in range(0,len(cpairs),2):
    if cpairs[i] > 0:
        temp_max_sum += calc_pos_row(matrix,cpairs[i],cpairs[i+1])
    else:
        temp_max_sum += calc_neg_row(matrix,cpairs[i],cpairs[i+1])
    if cpairs[i+1] > 0:
        temp_max_sum += calc_pos_col(matrix,cpairs[i],cpairs[i+1])
    else:
        temp_max_sum += calc_neg_col(matrix,cpairs[i],cpairs[i+1])
    sums.append(temp_max_sum)
    temp_max_sum = 0
max_sum = max(sums)
print(max_sum)

