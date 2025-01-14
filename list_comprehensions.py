# Write a list comprehension that creates a dictionary where the keys are the words
# and the values are the "average values" of those words. To calculate the average
# value you need to sum the letters of the word using their position in the english
# alphabet (a is 1, b is 2, c is 3 and so on) and divide it by the number of
# letters in the word. Round the result to 2 decimals at most and the keys
# should be in alphabetical order.)
# ["Vehicle", "Zebra", "X-ray", "Yellow", "Comprehension"] ->
# {'Comprehension': 11.85, 'Vehicle': 9.14, 'X-ray': 17.0, 'Yellow': 15.33, 'Zebra': 10.4}
def get_average(inp_string:str)->float:
    num_letters = 0
    lsum = 0
    for character in inp_string:
        if character.isalpha():
            num_letters+=1
            lsum += ord(character.upper())-64
    return round(lsum / num_letters,2)
lst = ["Vehicle", "Zebra", "X-ray", "Yellow", "Comprehension"]
lst.sort()
new_dict = {val:get_average(val) for val in lst}
print(new_dict)
# Output