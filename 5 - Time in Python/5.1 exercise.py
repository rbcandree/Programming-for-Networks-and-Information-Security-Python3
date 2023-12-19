#1 Write a program that prints the following information on screen:
# a) You are allowed to do certain operations on datetime objects. Create 2 separate datetime objects 
# that refer to different points in time and explore the results of following operations:
# dt_obj_1 - dt_obj_2
# dt_obj_1 < dt_obj_2
from datetime import datetime

dt_obj_1 = datetime.now()
dt_obj_2 = datetime(2023, 10, 12, 00, 00, 00)
td = dt_obj_1 - dt_obj_2
print(td)

verify = dt_obj_1 < dt_obj_2
print(verify)

# What can you tell about the - and < operators for datatime objects?
# Operator '-' allows to subtract one datetime object from another one and returns a timedelta object.
# Operators '>', '<' compares datetime objects as an integers and returns Boolean values: True or False.

# b) Current time in epoch format. What kind of operations are available for time represented in epoch format?
# Is Float, thus: (-, +, *, /, //, %, >, <) are available. 
# Convert the seconds since epoch to a more human readable format and print that also on screen.
from time import time, ctime
epoch_current_time = time()
epoch_time_example = 1598653800
print(epoch_time_example)
print(epoch_current_time)

human_readable_current_time = ctime(epoch_current_time)
print(human_readable_current_time)