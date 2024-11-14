
#1. is 和 is not用来比较是否是相同的对象，（内存地址?还是类型?)

#2. 逻辑判断中 not优先级最高， or优先级最低，
#所以 A and not B or C== ( A and (not B) ) or C

#3. 对于 or 而言，大概率为假的事件最好放在左边，可以短路快速运算
#   or 两者取其一

#4.逻辑运算符的多态（重载）？
#对于非布尔值类型的值，有如下顺序：
'''

 	Operation 	Result 	
法则 1 	x or y   	if x is true, then x, else y 	
法则 2 	x and y 	if x is false, then x, else y 	
法则 3 	not x  	        if x is false, then True, else False 	
'''
s1, s2, s3 = '', 'Trondheim', 'Hammer Dance'
s = s1 or s2 or s3
print( s)# s=='Trondheim'
# s = s1 or ( s2 or s3)
#   = s2 or s3  ( by 法则1)
#   = s2        (by 法则1）


