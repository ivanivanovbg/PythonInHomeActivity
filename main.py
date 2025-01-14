def calculate_bmi(weight, height):
    return round(weight / height ** 2, 2)


def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


import random, re, string


def generate_password(length):
    password = ""
    for i in range(length):
        password += random.choice(re.findall("[a-zA-Z0-9]", "aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890"))
    return password


def generate_password2(length):
    password = ""
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits)
    return password
