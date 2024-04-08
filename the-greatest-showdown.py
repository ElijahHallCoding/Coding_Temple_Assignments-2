# Task 1

# Prompting the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Identifying the largest number among the three
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Printing out the largest number
print("The largest number among", num1, ",", num2, ", and", num3, "is", largest)

# Task 2

# Identifying the smallest number among the three
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

# Printing out the largest and smallest numbers
print("The largest number among", num1, ",", num2, ", and", num3, "is", largest)
print("The smallest number among", num1, ",", num2, ", and", num3, "is", smallest)

# Task 3

# Checking for equality among the numbers
if num1 == num2 == num3:
    print("All numbers are equal.")
elif num1 == num2:
    print(f"Two numbers are equal and the largest. The numbers at positions 1 and 2 are equal.")
elif num1 == num3:
    print(f"Two numbers are equal and the largest. The numbers at positions 1 and 3 are equal.")
elif num2 == num3:
    print(f"Two numbers are equal and the largest. The numbers at positions 2 and 3 are equal.")
else:
    print("The smallest number is", smallest)
    print("The largest number is", largest)