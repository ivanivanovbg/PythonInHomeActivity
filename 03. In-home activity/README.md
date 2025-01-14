`1.` Write a function that calculates and returns the Body Mass Index (BMI) based on height (in meters) and weight (in kilograms). The function should return the result rounded to two decimal places. The formula for calculating BMI is weight divided by height squared.
```py
x = calculate_bmi(70, 1.75)  # bmi should be approximately 22.86
x = calculate_bmi(85, 1.8)   # bmi should be approximately 26.23
```

`2.` Write a function that returns the largest number from a given list of numbers, without using the build-in function max.
```py
x = find_largest([1, 2, 3, 4, 5])  # largest should be 5
x = find_largest([-10, -2, -3, -6])  # largest should be -2
```

`3.` Write a function that converts a number of seconds into a formatted time string "hours:minutes:seconds".
```py
x = seconds_to_time(3661)  # x should be "01:01:01"
x = seconds_to_time(45)    # x should be "00:00:45"
```

`4.` Write a function generate_password that creates a simple, random password consisting of letters and digits. You will need to find out how "random" works.
```py
x = generate_password(8)  # password could be "aB3dE4fG"
x = generate_password(12) # password could be "Hk9Pv4wBz2Lq"
```

