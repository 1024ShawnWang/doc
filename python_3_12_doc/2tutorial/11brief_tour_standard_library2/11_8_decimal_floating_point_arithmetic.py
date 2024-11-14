
#比float更加精准的类型，暂且略过吧。float我都没用到

from decimal import *
#0.7*1.05 ==0.735
print( round( Decimal('0.70') * Decimal('1.05'), 2) ) #1.取两位有效数字，会四舍五入

r1 =round( 0.70*1.05, 2) #2.对比普通的float类型，会全舍弃，直接输出 0.73
print( r1)

