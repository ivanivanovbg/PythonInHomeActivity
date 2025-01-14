def func():
    global number
    number += 1
    return number

number = 1
print(func())