# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 6/21/2022
# Description: Asks user to input degrees C and converts it to F.

print("Please enter a Celsius temperature.")
temp = float(input())
conversion = ((9 / 5) * temp + 32)
print("The equivalent Fahrenheit temperature is:\n")
print(conversion)
