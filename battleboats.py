output = []
rows,cols = list(map(int,input().split()))
players = [[],[]]
for row in range(rows):
    players[0].append([int(x) for x in input().split()])
for row in range(rows):
    players[1].append([int(x) for x in reversed(input().split())])
players[1] = players[1][::-1]
command = input()
moves = 1
while command != "END":
    shoot_row,shoot_column = list(map(int,command.split()[1::]))
    if players[moves % 2][shoot_row][shoot_column] == 1:
        players[moves % 2][shoot_row][shoot_column] = -1
        output.append("Booom")
    else:
        if players[moves % 2][shoot_row][shoot_column] == 0:
            players[moves % 2][shoot_row][shoot_column] = -1
            output.append("Missed")
        else:
            output.append("You already shot there!")
    moves+=1
    command=input()
score_player1 = 0
score_player2 = 0
for i in range(len(players[0])):
    for j in range(len(players[0][i])):
        if players[0][i][j] == 1:
            score_player1 += 1
        if players[1][i][j] == 1:
            score_player2 += 1
output.append(str(score_player1)+":"+str(score_player2))
print("\n".join(output))