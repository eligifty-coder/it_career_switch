colors = ["blue", "red", 'yellow', "green"]
num = [23,100,15,225, 5, 71]

#sort  Alphabetically
num.sort()
colors.sort()
print(num)
print(colors)

# reverse Alphabetically
# num.reverse()
# colors.reverse()
# OR
num.sort(reverse=True)
colors.sort(reverse=True)

# sorted func, maintains original list
my_colors = ["purple", "teal","white","black"]
sorted_colors =  sorted(my_colors)

print(my_colors)
print(sorted_colors)
# print(num)