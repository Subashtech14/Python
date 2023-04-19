#In python there are two types of file text and binary
#Crud Operations -> create,Read,Update,Delete
#Flow Create File -> Open File -> Work -> Close File
#open(filename, mode)
#default mode is read mode
#"r" - Read - Default value. Opens a file for reading.error if the file doesn't exist
#"a" - Append - Opens a file for appending. Creates the file if it doesn't exist
#"w" - Write - Opens a file for writing. creates the file if it doesn't exist.
#"x" - Create - Creates the specific file,returns an error if the file exists
#We can specify if the file should be handeled as a binary or text mode
# "t" - Text - Default Value. Text Mode
# "b" - Binary - Binary mode. (e.g images)
#readline() reads it line by line
#readline(3) Reads the third line only
#readlines() Read lines separately
file=open("E:\\Python\\Devil.txt","a")
file.write("I Have Woken up child from now on i will take control ")
file.write("I will kill yoy")
file.close()
file=open("E:\\Python\\Devil.txt","r")
print(file.read())
file.close()
file=open("E:\\Python\\Devil.txt","r")
print(file.readlines())
file.close()
print("Looping through a File \n")
#Loop over a file Object
file=open("E:\\Python\\Devil.txt","r")
for line in file:
    print(line)
file.close()
#writing to a file
#"a" Append -Will append to the end of the file
#"w" Write will overwite any existing file
file=open("E:\\Python\\Devil.txt","a")
file.write("I have become the devil")
file.close()
#Creating a file
#"x" - Create  - will create a file,returns an error if the file exist
#"a" Append - Will create a file if it doesn't exist
#"w" Write will create a file if it doesn't exist
#Deleting a File
import os
if os.path.exists("Devil.txt") or os.path.isdir("kill"):
    os.remove("Devil.txt")
    os.rmdir("kill")
else:
    print("The File Doesn't exist")