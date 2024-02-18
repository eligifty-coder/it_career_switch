with open("demo.txt") as myFile:
   contents = myFile.read()
   print(contents)


a = open("demo.txt","w")
a.write("What has happened now!")
a.close()

print("-----------------------------------------------------")

with open('demo.txt') as myfile:
   contents= myfile.read()
   print(contents)


# CREATE A NEW FILE
# y = open('daveFile.txt','x')
# y.close()

#1 PRACTICE
open('tutor.txt','x') 

file_txt = open('tutor.txt','w')
file_txt.write("What in the world happened!! Oh my God!!")
file_txt.close()

with open('tutor.txt','r') as myReadFile:
   myReadFile.read()
   print(myReadFile)


#2 PRACTICE
counter =0
with open('newFile.txt','a') as a_file:
   while counter <3:
      a_file.write(f"you are my hubby x {counter}\n")
      counter+=1
   
with open('newFile.txt', 'r') as read_file:
   print(read_file.read())