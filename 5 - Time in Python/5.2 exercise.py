#2  Given a string "2020-09-28  18:47:50", convert the string into a datetime object. 
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta 

date_as_str = "2020-09-28 18:47:50"
format_str = "%Y-%m-%d %H:%M:%S"
date_obj = datetime.strptime(date_as_str, format_str)
print(date_obj)

#   Access the objects year, month, day and hour attributes separately and print the result on screen.
year = date_obj.year
month = date_obj.month
day = date_obj.day
hour = date_obj.hour
print(year, month, day, hour) 

#   Raise all of these values by one.
date_obj = date_obj + relativedelta(years = 1)
date_obj = date_obj + relativedelta(months = 1)
date_obj = date_obj + timedelta(days = 1)
date_obj = date_obj + timedelta(hours = 1)
print(date_obj)

#   Convert the resulting datetime object into a string of format YYYY-mm-dd HH:MM:SS.
date_obj_convert = date_obj.strftime("%Y-%m-%d %H:%M:%S")
print(date_obj_convert)

#   Do the same conversion but with the resulting string in format: 
#   'It's year 2021, day 29 of month 10 and it is 19:47:50.'
date_obj_convert1 = date_obj.strftime("It's year %Y, day %d of month %m and it is %H:%M:%S.")
print(date_obj_convert1)