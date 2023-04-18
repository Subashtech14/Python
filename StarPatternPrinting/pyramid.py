#Pyramid
def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\n")
pattern(5)
print("Inverse Pyramid\n")
#Inverse Pyramid
def Ipattern(n):
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ",end="")
        print("\n") 
Ipattern(5)
print("Left half pyramid pattern\n")
#Left half pyramid pattern
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(10)
print("Right half pyramid\n")
#Right half pyramid
def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(10)
print("Downward half pyramid\n")
#Downward half pyramid
def pattern(n):
    for i in range(n,-1,-1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(10)

print("Diamond pattern \n")     
def pattern(n):
    k=2*n-2 
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    k=n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
pattern(10)
        
         