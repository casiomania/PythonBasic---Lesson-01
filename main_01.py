# Lesson 01 / Homework 01
# The user enters three numbers from the keyboard. It is necessary to find the sum of numbers, the product of numbers.
# Display the result of the calculation on the screen.

entered_number = int(input("Enter 3-digit number: "))

number_1 = entered_number // 100 % 10
number_2 = entered_number % 100 // 10
number_3 = entered_number % 10

result_1 = number_1 + number_2 + number_3
result_2 = number_1 * number_2 * number_3

print(f"number1: {number_1} number2: {number_2} number3: {number_3}")
print(f"Sum: {result_1}")
print(f"Product: {result_2}")