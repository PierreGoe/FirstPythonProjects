# import time


# print(time.strftime("%Y-%m-%d"))
# time.sleep(5)




import datetime 



d1 = datetime.datetime(2018, 8, 25, 14, 50, 00,)
d2 = datetime.datetime(2018, 8, 25, 15, 50, 00,)

d3 = d2-d1
print(d3)

d1 = datetime.date(2018, 8, 25,)
from datetime import datetime
print(datetime.now())