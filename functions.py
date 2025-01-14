"""

1. Write a function that sums only the digits in a string

x = sum_digits('abc123a4') # x = 10
x = sum_digits('abc') # x = 0
2. Write a function that 'merges' two equal length numbers. The merging operation adds the digits that are in the same positions and if the result is greater than 9, only the last digit remains. So 1 + 2 = 3, but 8 + 5 = 3 also.

x = merge(123, 123) # x = 246
x = merge(789, 123) # x = 802 (7 + 1 = 8, 8 + 2 = 10, 9 + 3 = 12)
3. Write a function that counts the number of occurrences of a letter in a string.

x = occurrences('a', 'aaa') # x = 3
x = occurrences('a', 'aabb') # x = 2
x = occurrences('a', 'bbcc') # x = 0
4. Write a function that returns the letter which occurs more often than another letter in a text. Use the function from the previous exercise.

x = stronger_letter('abca', 'a', 'b') # x = 'a'
x = stronger_letter('abbca', 'c', 'b') # x = 'b'
x = stronger_letter('aabbc', 'b', 'a') # x = 'b' (return the first one in case of a tie)
5. Write a function that determines if three numbers (representing lengths of sides) can form a triangle. To form a triangle the largest side must be smaller than the sum of the other two. You do not know which of the three parameters will be the largest.

x = can_form_triangle(3,4,5) # x = True
x = can_form_triangle(3,6,3) # x = False

"""
import random


def sum_digits(input_string):
    number_sum = 0
    for character in input_string:
        if character.isdigit():
            number_sum += int(character)
    return number_sum

def merge(num1,num2):
    str_number1 = str(num1)
    str_number2 = str(num2)
    str_result = ""
    for i in range(len(str_number1)):
        temp_res = int(str_number1[i]) + int(str_number2[i])
        if temp_res > 9:
            str_result += str(temp_res - 10)
        else:
            str_result += str(temp_res)
    return int(str_result)

def occurrences(char_search,input_string:str):
    return input_string.count(char_search)

def stronger_letter(input_string,char1,char2):
    if occurrences(char1,input_string) >= occurrences(char2,input_string):
        return char1
    else:
        return char2

def can_form_triangle(a,b,c):
    if max(a,b,c) < (a+b+c) - max(a,b,c):
        return True
    else:
        return False
"""
1. Write a function that calculates and returns the Body Mass Index (BMI) based on height (in meters) and weight (in kilograms). The function should return the result rounded to two decimal places. The formula for calculating BMI is weight divided by height squared.

x = calculate_bmi(70, 1.75)  # bmi should be approximately 22.86
x = calculate_bmi(85, 1.8)   # bmi should be approximately 26.23
2. Write a function that returns the largest number from a given list of numbers, without using the build-in function max.

x = find_largest([1, 2, 3, 4, 5])  # largest should be 5
x = find_largest([-10, -2, -3, -6])  # largest should be -2
3. Write a function that converts a number of seconds into a formatted time string "hours:minutes:seconds".

x = seconds_to_time(3661)  # x should be "01:01:01"
x = seconds_to_time(45)    # x should be "00:00:45"
4. Write a function generate_password that creates a simple, random password consisting of letters and digits. You will need to find out how "random" works.

x = generate_password(8)  # password could be "aB3dE4fG"
x = generate_password(12) # password could be "Hk9Pv4wBz2Lq"
"""

def calculate_bmi(weight:float,height:float):
    return round(weight / ( height*height),2)

def find_largest(num_list):
    largest = num_list[0]
    for number in num_list:
        if number > largest:
            largest = number
    return largest

def seconds_to_time(seconds:int):
    hours = seconds // 3600
    minutes = (seconds - hours*3600)//60
    secs = seconds - hours*3600 - minutes*60
    return str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(secs).zfill(2)

def generate_password(length):
    password_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    final_password = ""
    for i in range(length):
        final_password += password_chars[random.randint(0,len(password_chars))]
    return final_password

