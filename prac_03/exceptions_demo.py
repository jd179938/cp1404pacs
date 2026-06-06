"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When an input for the denominator or the numerator is anything but numeric values (eg a,%,,)
or one value has a decimal values

2. When will a ZeroDivisionError occur?
When the denominator is entered as 0 (although this error will not occur when the numerator
is entered as 0, this will print 0 for all values of the denominator)

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")