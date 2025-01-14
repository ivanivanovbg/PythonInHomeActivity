inp_row_col = input()
rows = int(inp_row_col.split()[0])
cols = int(inp_row_col.split()[1])
res = 1

def is_corner(current_i:int,current_j:int,max_i:int,max_j:int)->bool:
    if (current_i == max_i-1 and current_j == max_j-1) or (current_i == 0 and current_j == max_j-1) or (current_i == max_i-1 and current_j == 0):
        return True
    else:
        return False

def do_movement():
    global i,j,direction
    if ( i == rows-1 ) or ( j == cols-1) or ( j == 0 and i != 0 ) or ( i == 0 and j != 0):
        direction += 1
    if direction % 4 == 1 or direction % 4 == 0:
        i += 1
    else:
        i -= 1
    if direction % 4 == 1 or direction % 4 == 2:
        j += 1
    else:
        j -= 1

i = 0
j = 0
direction = 1

while not is_corner(i,j,rows,cols):
    do_movement()
    res += 2**(i+j)

print(res)
