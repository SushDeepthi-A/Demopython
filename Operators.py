# Added extra functionality to the exisitng code to implement the operators in python file
a=5
b=3
print("Addition of a and b",a+b)
print("Subtraction of a and b",a-b)
print("Multiplication of a and b",a*b)
print("Division of a and b",a/b)
print("floor division of a and b",a//b)
print("Modulus of a and b",a%b)
print("Exponenation of a and b",a**b)
#Logical Operators
print("Logical AND Operation of a and b",a>b and a>=b)
print("Logical OR Operation of a and b",a>b or a>=b)
print("Logical NOT Operation of a and b",not(a > 3 and b < 10))
#Bitwise Operators
print("Bitwise AND Operation of a and b", a & b)
print("Bitwise OR Operation of a and b", a | b)
print("Bitwise NOT Operation of b",~b)
print("Bitwise XOR Operation of a and b",a^b)
print("left shift",a<<b)
print("Right Shift",a>>b)
#Comparision operators
print("A is Greater than B", a>b)
print("B is Greater than a", b>a)
print("A is Greater than or equal B", a>=b)
print("A is Less than or equal B", b>a)
print("A is Equal to B", a==b)
print("A is not Equal to B", a!=b)
#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

##Membership Operator

x = ["apple", "banana"]

print("pineapple" not in x)

# returns True because a sequence with the value "pineapple" is not in the list
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list
