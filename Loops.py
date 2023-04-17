#Loops allows the execution of a statement or a group of statement multiple times
#while for Nested
#While
#While loops are known as indefinite or conditional loops. They will keep iterating until certain
#conditions are met. There is no guarantee ahead of time regarding how many times the loop will iterate.
count=0
while count < 9:
    print("Number : ",count)
    count+=1
print("Good Bye")
#For Loop is a python loop which repeats a group of statements a specified number of times.
#The for loop provides a syntax where the following information is provided
#Boolean Condition
#The initial Value of the counting variable
#Incrementation of counting variable
fruits=["Mango","Grapes","Apple"]
for fruit in fruits:
    print("Current Fruit ",fruit)
#Code to print the pythagorean numbers
from math import sqrt
n=int(input("Maximal Number? "))
for a in range(1,n+1):
    for b in range(a,n):
        c_square=a**2+b**2
        c=int(sqrt(c_square))
        if((c_square - c**2)==0):
            print(a ,b ,c)