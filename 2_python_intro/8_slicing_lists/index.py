players = ["bob", 'steve','michael', 'tom', 'eli', 'bill','dave']

for player in players[2:8]:
   print(player.title())

nums = [1,2,3,4,5,6,7,8,9]
print(nums[2:8:2])
# 1>> starting index
# 8 >>slice until the this index
# 2 >>> slicing increment ie take 2 steps then slice

# PRACTICE TIME
names = ['elijah','gift','elizabeth','samuel','anthony','evelyn', 'rejoice', 'bobo']
sliced_names = names[2:5]
print(sliced_names)

numbers = [22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
odd_nums = numbers[1:len(numbers):2]
print(odd_nums)