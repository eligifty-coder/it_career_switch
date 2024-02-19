import sys
try:
   print(0/0)
except ZeroDivisionError:
   print("You ")

try:
   num  = int(input("Enter a number between 1-10 "))
except ValueError:
   print("Please use numbers only")
   sys.exit()
print(f"You entered the number: {num}")