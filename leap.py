year = int(input("Enter your year: "))

# Check if the year is divisible by 4 but not by 100, or if it is divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
