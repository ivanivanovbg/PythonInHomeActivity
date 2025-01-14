start_pos = int(input())
inp_arr = list(map(int,input().split(",")))
inp_cmd = input()
forward = 0
backwards = 0
cmds = 10000*[None]
i = 0
linp = len(inp_arr)
while not inp_cmd == "exit":
    cmds[i] = inp_cmd
    inp_cmd = input()
    i+=1
for inp_cmd in cmds:
    if not inp_cmd is None:
        command = inp_cmd.split()
        cmd_dir = command[1]
        cmd_steps = int(command[0])
        cmd_steps_size = int(command[2])
        if cmd_dir == "forward":
            for i in range(cmd_steps):
                start_pos += cmd_steps_size
                while start_pos >= linp:
                    start_pos -= linp
                forward += inp_arr[start_pos]
        else:
            for i in range(cmd_steps):
                start_pos -= cmd_steps_size
                while start_pos < 0:
                    start_pos += linp
                backwards += inp_arr[start_pos]
    else:
        break

print(f"Forward: {forward}")
print(f"Backwards: {backwards}")