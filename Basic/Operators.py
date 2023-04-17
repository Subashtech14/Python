#Types of Operators
#Arithmetic 
#Assignment
#Comparison
#Logical
#Membership
#Identity
#Bitwise
#Arithmetic operatoes are used to perform arithmetic Operations between variables.
x=10
y=20
print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x/y)
print(x//y)
print(x%y)
#Assignment Operators
#Assignment Operators are used to assign values
#=,+=,-=,*=,%=,**=,//=,|=,^=,&=
x=10
#Comparison Operators
#Comparison Operators are used to compare two values
#== != > >= < <=
print(x==y)
#Coniditional statements
#if elseif else
val=10
num=11
if val==num:
    print("equal")
elif val > num:
    print("val is greater")
else:
    print("num is greater")
#Logical operators
#Logical Operations are used to combine conditional statements  
print(val > 10 and val==10)  
print(val < 10 and val==10)  
print(not(x>10))
#Identity Operators
#Identity Operators are used to compare objects
#is returns true if both the objects are same 
#isnot returns true if both the objects are same
list1=[10,20,30]
a=list1
list2=[10,20,30]
print(a is list1)
print(list2 is list1)
#Membership Operators
#Membership Operators are used to check if a sequence is present in an object.
#in not in
print("Membership operators")
print(10 in list1)
print(11 in list1)
#Bitwise Operators
#Bitwise Operators are used to compare binary numbers
#& Bitwise AND sets each bit to 1 if both bits are 1
#| Bitwise OR sets each bit to 1 if none of the bits is 1
#^ Bitwise XOR sets each bit to 1 if only one of the bits is 1
#~ Bitwise NOT Inverts all bits
#<< Left Shift Shift left by pushing in zeros from the right and let the leftmost bits fell off
#>> Right Shift shift right by pushing copies of the left most bit in from the left, and let the right most bit fall off.
print(10&12) #10=1010 12=1100 the resulting bit is 1000
print(10|12) #10=1010 12=1100 the resulting bit is 1111