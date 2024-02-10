# Lesson 01 / Homework 03
# The user enters a four-digit number from the keyboard. You need to find the product of the numbers.
# For example, if 1324 is entered from the keyboard, then the result will be - 1*3*2*4 = 24.

entered_number = int(input("Enter 4-digit number: "))

number_1 = entered_number // 1000
number_2 = entered_number // 100 % 10
number_3 = entered_number % 100 // 10
number_4 = entered_number % 10

result_1 = number_1 * number_2 * number_3 * number_4

print(f"number1: {number_1} number2: {number_2} number3: {number_3} number4: {number_4}")
print(f"Product: {result_1}")
