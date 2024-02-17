employees = ["sara", "tammy", "debbie", "john", "carrie"]
employees = employees + ["jim"]
# print(employees)
fav_nums = ['16', '24', '7', '100']
fav_colors = ['blue', 'red','green', 'pink']
print(fav_nums + fav_colors)

employees.insert(1, "dave")

del employees[4]
# OR

employees.remove('carrie')
# print(employees)

# looping through a list in python
for x in employees:
   print(x)

if "tammy" in employees:
   print("yup!!, Tammy works here")

# print(len(employees))

# practice
fam = ["hubby", 'mum','fathers', 'sibling', 'friends']
fam[3] = 'two fathers'

del fam[2]
fam.insert(3,'mum')
print(fam)