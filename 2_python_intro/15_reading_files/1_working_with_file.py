
# Files  can also be opened in python with the "with" keyword. this automatically opens and closes the file once ypu are done . It eliminates the use of close() which might be advantageous if the program has a bug and never reaches the close() method


# Reading file
print("Reading file")
print("--------------------------------------------------")
a = open("demo.txt", 'r') 
print(a.read())
print("next print")
a.close()

print("--------------------------------------------------")
a = open("demo.txt", 'r')
print(a.readline())
print("next print")
a.close()

print("--------------------------------------------------")
a = open("demo.txt", 'r')
print(a.read(7))
print("next print")
a.close()

# Files  can also be opened in python with the "with" keyword. this automatically opens and closes the file once ypu are done . It eliminates the use of close() which might be advantageous if the program has a bug and never reaches the close() method
print("--------------------------------------------------")

with open("demo.txt","a") as myfile:
   contents = myfile.write("\n Here's is another line in our text file")
   print(contents)

print("--------------------------------------------------")

with open("demo.txt") as myfile:
   contents = myfile.read()
   print(contents)
   

