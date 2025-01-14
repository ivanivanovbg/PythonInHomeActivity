def dir_change(im:[[]],current_i:int,current_j:int,d_i:int,d_j:int)->int:
    ms = len(im) - 1
    if (current_i == 0 and current_j == ms) or (current_i == ms and current_j == ms) or (current_i == ms and current_j == 0):
        return 1
    else:
        if not im[current_i + d_i][current_j + d_j] == "X":
            return 1
        else:
            return 0

def fill_matrix(im:[[]]):
    moves = 1
    direction = 1
    """
    direction :
    1 - left -> right
    2 - up -> down
    3 - right -> left
    4 - down -> up
    """
    i = 0 #starting row
    j = 0 #starting column
    di = 0
    dj = 1
    while moves <= len(im)*len(im):
        im[i][j] = moves
        direction += dir_change(im,i,j,di,dj)
        dir_rem = direction % 4
        if dir_rem == 1:
            di = 0
            dj = 1
        elif dir_rem == 2:
            di = 1
            dj = 0
        elif dir_rem == 3:
            di = 0
            dj = -1
        else:
            di = -1
            dj = 0
        i += di
        j += dj
        moves += 1

            

inp_matrix_side = int(input())
matrix = [["X"]*inp_matrix_side for i in range(inp_matrix_side)]
fill_matrix(matrix)
for i in range(len(matrix)):
    print(*matrix[i],sep=" ")