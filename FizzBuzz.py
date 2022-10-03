# FizzBuzz assignment
# Erik Do
# This will create a for loop from 1 to 100
for i in range(1, 100):
    # If Python finds any integer that is divisible by 15, create a string called FizzBuzz
    if i % 15 == 0:
        print("FizzBuzz")
    # If Python finds any integer that is divisible by 3, create a string called Fizz
    elif i % 3 == 0:
        print("Fizz")
    # If Python finds any integer that is divisible by 5, create a string called Buzz
    elif i % 5 == 0:
        print("Buzz")
    # Otherwise, Python will print the integer without any strings
    else:
        print(i)