#4  a) Find out programmatically which day of the week was on 1.10.1999
from datetime import datetime, timedelta
from time import ctime

dt_obj_a = datetime(1999, 10, 1, 0, 0, 1)
epoch_time = dt_obj_a.timestamp()
conv = ctime(epoch_time)
print(f"What day of the week was October 1st, 1999? It was {conv[0:3]}.")

#   b) Find out programmatically which day is 27 weeks before 1.10.1999
dt_obj_b = dt_obj_a - timedelta(weeks = 27)
week_day = dt_obj_b.strftime('%A')
date = dt_obj_b.strftime('%d')
month = dt_obj_b.strftime('%B')
print(f"Which day was it 27 weeks before October 1st, 1999?\nIt was {week_day}, {date}th of {month}.")

#   c) Find out programmatically which day of the week is 157 days after 1.10.1999
dt_obj_c = dt_obj_a + timedelta(days = 157)
week_day_c = dt_obj_c.strftime('%A')
print(f"Which day of the week is 157 days after October 1st, 1999? It is {week_day_c}.")
# *Hint: strftime() method may help you with these.