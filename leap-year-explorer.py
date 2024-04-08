# Tasl 1: Leap Year Checker

# Prompt the user to input a year
year = int(input("Enter a year: "))

# Check if the entered year is a leap year
if year % 4 == 0:  # Check if the year is divisible by 4
    if year % 100 == 0:  # Check if it's a centurial year
        if year % 400 == 0:  # Check if it's divisible by 400
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")