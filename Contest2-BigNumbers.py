def get_addition(has_addition:bool)->int:
    # Custom function that returns int -> 1 if there is an addition and int -> 0 if there is no addition
    if has_addition:
        return 1
    else:
        return 0

def add_number_arrays(num1_arr:[int],num2_arr:[int])->[int]:
    # Get the max length of the two lists
    max_length = max(len(num1_arr),len(num2_arr))
    # Append Number of elements corresponding to the difference between max_length and the number of elements in the
    # specific list thus ensuring that when iterating we'll not get an exception
    num1_arr += (max_length-len(num1_arr))*[0]
    num2_arr += (max_length-len(num2_arr))*[0]
    # The list containing the result should be max_length + 1 in case the sum of the two big numbers exceeds max_length
    # For example
    # 5 5 5
    # +
    # 6 5 5
    # =
    # 1 1 1 1 <-- length is ( 4 ) greater than length ( 3 ) of  both input numbers
    res = (1 + max_length) * [0]
    # Define a bool telling us if the last addition has resulted in a number greater than 10, by default - Not
    addition = False
    # Iterate through both numbers and add their digits
    for i in range(max_length):
        # Calculate the sum of the two current digits and the resulting addition from previous operation
        add_res = num1_arr[i] + num2_arr[i] + get_addition(addition)
        # If the sum is greater than 9 then subtract 10 and set the addition variable to True to ensure correct
        # execution of next operation
        if add_res > 9:
            res[i] = add_res - 10
            addition = True
        else:
            res[i] = add_res
            addition = False
    # When the function has finished looping through all the digits of the two numbers we may have an addition remaining from
    # the last operation, if this is the case add 1 as the first digit of the result.
    # We only need 1 or 0 because if we add for example two three-digit numbers ( max 999 ) the resulting
    # Four digit number will be maximum 1998
    # For example
    # 9 9 9
    # +
    # 9 9 9
    # =
    # 8 9 9 1 <-- Maximum value of 1 for the first digit
    if addition:
        res[max_length] = get_addition(addition)
    else:
    # If we don't have a 1 as the first digit remove it from the array, because the big bad judge will punish us ;(
        res.pop()
    return res

def main():
    # First input line gives us the length of the numbers ( lists ) , but the logic of the program will be such that
    # we will not need it :)
    dummy_line = input()
    # Split the input ( default separator is whitespace, hence no arguments for split() function )
    # Map the split values to ints and turn them into a list
    num1 = list(map(int,input().split()))
    num2 = list(map(int,input().split()))
    # Call custom function add_number_arrays with arguments num1,num2
    # The task requires a specific output format, so the list must be unpacked ( * )
    # in order to match the output requirements
    print(*add_number_arrays(num1,num2),sep=" ")

main()

