import shutil

# operating system (os) module
import os


src = 'demo.txt'
dst = 'davedemo.txt'
shutil.copy(src, dst)

os.rename('davedemo.txt', 'leaveMeAlone.txt')
# os.remove('leaveMeAlone.txt')

#1 PRACTICE
src = 'leaveMeAlone.txt'
dst = 'practicedemo.txt'
shutil.copy(src, dst)
os.rename('practicedemo.txt', 'practicedemo1.txt')

print("------------------------------------------------")
#2 PRACTICE

with open('newFile.txt', 'x') as assignedFile:
   print('g')


with open('newFile.txt', 'a') as assignedFile:
   assignedFile.write("\n Abba has given me that which my heart desires")

src = 'newFile.txt'
dst = 'writtenFile.txt'
shutil.copy(src,dst)

with open(dst,'a') as files:
   files.write("\nIt career switch pyton course")

