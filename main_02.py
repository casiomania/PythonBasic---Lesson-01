# Lesson 01 / Homework 02
# Write a program that calculates the area of a rhombus. The user enters the length of its
# two diagonals from the keyboard. The area of a rhombus is equal to half the product of its diagonals: S = (AC · BD)/2.

first_diagonal = int(input("Enter the first diagonal: "))
second_diagonal = int(input("Enter the second diagonal: "))
rhombus_area = (first_diagonal * second_diagonal) / 2
print("Rhombus area", rhombus_area)
