import time
print(time.ctime(0)) #date from which the computer measures system time
print(time.time()) #seconds in time since the reference point or since epoch
print(time.ctime(time.time())) #prints the current time

time_object = time.localtime()
print(time_object)
time.strftime("%B %d %Y %H %M %S", time_object)