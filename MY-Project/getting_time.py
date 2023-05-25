import datetime
import time

current_time = datetime.datetime.now()


print("\n Time is in 24 hour format \n")
a = int(input("Enter the Hour : "))
b = int(input("Enter the minute : "))

loop = 5
while loop > 0:
	print("current hour : ", current_time.hour)
	print("current minute : ", current_time.minute)
	print("current second : ", current_time.second)
	time.sleep(5)	
	loop = loop - 1
	# if current_time.minute == b:
	# 	loop = False


