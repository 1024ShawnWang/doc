
from timeit import Timer   #1.用来计算语句执行所需要的时间

#比较多重赋值语句和完成相同目标的多个单赋值语句
s=Timer( 'a, b= b,a', 'a=1;b=2').timeit()  #多重赋值
t=Timer( 't=a; a=b; b=t', 'a=1;b=2').timeit()#单赋值
print( s, t)
