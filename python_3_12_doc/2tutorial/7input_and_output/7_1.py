
year = 2024
event = 'Referendum'
print( f'Results of the {year} {event}' )# 1. 字符串前面加f ,f for formate

yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes/total_votes
print( '{:-9} YES votes {:2.2%}'.format( yes_votes, percentage) )# 2.字符串后面使用.format()方法

import math
print( 'The value of pi is approximately %5.3f.' %math.pi ) #3.使用%符号
        
