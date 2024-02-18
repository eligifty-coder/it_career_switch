# to receive information through the keyboard, python uses either the input() or raw_input()
# input() >>> is python 3.0
# raw_input >>> is python 2.0


text = input("Hey!! can you see this Yes or No?\n")
print(f"you said {text}")

txt = input("Give me a number: ")
try:
   num =  int(txt)
except ValueError:
   print("Please put in a real number, not  a string or a text")
   print(f"the number you gave is: {num}")