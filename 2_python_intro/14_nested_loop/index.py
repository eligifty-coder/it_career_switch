# A nested loop is a loop inside a loop
# The "inner loop" will be executed one time for each iteration of the "outer loop" 
outer = ["outer1", "outer2","outer3"]
nest = ["nest1","nest2", "nest3"]

for x in outer:
   for y in nest:
      print(x,y)
   print("\n")

print("---------------------------------------------------")
numbers = [1,2,3]
letters = ['a','b','c']

for x in numbers:
   print(x)
   for y in letters:
      print(y.upper())
   print("\n")

# PRACTICE TIME
leads = ["mark",'bob','sara']
departments =["it","public relation", 'human resources', 'sales', 'administration']

for x in leads:
   print(x.upper())
   for y in departments:
      print(y)
   print("\n")