# Now you write the rest.

# Your program should print:

# Sum
# Difference
# Product
# Division
# Floor Division
# Remainder
# Power
# Example

# If the user enters:

# 10
# 3

# Your output should look something like:

# ========================================
# CALCULATOR
# ========================================
# First Number  : 10.0
# Second Number : 3.0

# Addition       : 13.0
# Subtraction    : 7.0
# Multiplication : 30.0
# Division       : 3.3333333333333335
# Floor Division : 3.0
# Remainder      : 1.0
# Power          : 1000.0
# ========================================



num1= float(input("Enter the first Number : "))
num2= float(input("Enter the second Number : "))

print("="*40)
print("Calculator".center(40))
print("="*40)
print(f"First Number : {num1}")
print(f"Second Number : {num2}")
print()
addition = num1+num2
subtraction = num1-num2
multiplication = num1*num2
division = num1/num2
floor_division = num1//num2
remainder = num1%num2
power = num1**num2 
print (f"Addition         : {addition}")
print (f"Subtraction      : {subtraction}")
print (f"Multiplication   : {multiplication}")
print (f"Division         : {division:.2f}")
print (f"Floor Division   : {floor_division:.2f}")
print (f"Remainder        : {remainder:.2f}")
print (f"Power            : {power:.2f}")
print("="*40)



