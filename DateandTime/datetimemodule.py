#datetime module
#datetime() Datetime constructor
#datetime.today() -> Returns the current date and time
#datetime.now() -> Returns the current date and time
#date() -> takes year,month,and day as paramater and creates the corresponding date
#time() -> takes hour,min,sec,microseconds and tzinfo as paramater and creates the corresponding 
#datetime.fromstamp() -> converts seconds to return the corresponding date and time
#timedelta() -> It is the difference between different dates or times(Duration)
import datetime
print(datetime.datetime.today())
print(datetime.date(2019,7,5))
print(datetime.time(3,45,23))
b1=datetime.timedelta(days=20)
b2=datetime.timedelta(days=30)
b3=b1-b2
print(b3)
print(type(b3))