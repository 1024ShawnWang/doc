from datetime import date
now =date.today()
print( now)


print( now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.") ) #1. datetime对象转为字符串, 
#09-22-24. 22 Sep 2024 is a Sunday on the 22 day of September.
#m:month    d:days  y:year  b:月份简称  A:星期几    B:月份全称


