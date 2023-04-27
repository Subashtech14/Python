#The time module
#Begins recording time from the epoch that begins at 00:00:00 1st january 1970
#time() -> Returns the number of seconds
#ctime() -> Returns the current date and time
#sleep() -> stops the execution of a thread for the given duration
#localtime() -> Returns the data and time in time.struct_time format
#gmtime() -> Returns time.struct_time in UTC Fromat
#mktime() -> Return sthe seconds passed since epoch pas output
#asctime() -> Returns a string representing the same
import time
print(time.time())#current seconds from the epoc
print(time.ctime())#current date and time
a=time.localtime()
b=time.mktime(a)
print(b)
c=time.asctime(a)
print(c)
#print(help(time.strftime))
print(a)
x=time.strftime("%m/%y/%Y")
print(x)
y="08 August 2019"
s=time.strptime(y,"%d %B %Y")
print(s)