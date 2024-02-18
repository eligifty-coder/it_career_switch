# IDENTITy operators
# It is used to compare the object, not if they are equal, but if they are actually the same object, with the same memory location
a =2
b=6
c =a
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)

print("-----------------------------------------------")

# MEMBERSHIP operator
# in and not in
numbers = [1,2,3,4]
print(2 in numbers)
print(2  not in numbers)

print("-----------------------------------------------")

colors = ['blue','red','yellow']
print("green" in numbers)

print("-----------------------------------------------")

# BITWISE OPERATORS
# bitwise operators are used to compare binary numbers
# &:(AND), |:(OR),  ^ :XOR(set to 1 if only one is 1)
a =24
b=60
print(bin(a))
print(bin(b))

a =24
b = 60
a & b
x = 223
y = 111
print(a | b)


