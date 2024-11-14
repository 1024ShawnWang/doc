
#1.提供了对运算符，比如 +，=，下，/的重写，比较，逻辑，数学运算，序列运算。优点是？。。

#2. operator.lt(a,b) #less than 严格小
#2.1 le(a,b) #less than and equal 
#2.2 eq(a,b)
#2.3 ge(a,b)
#2.4 gt(a,b)

#3. operator.not( obj)

#4. operator.truth(obj)  ojb为真值就返回True，否则False

#5. operator.is_(a, b) 返回 a is b的结果

#6. operator.is_not(a, b) 

#数学运算 
#7. operator.abs( obj) #绝对值

#8. operator.odd( a, b)

#9. .and_(a, b)  类比 & 按位与

#10. floordiv( a, b) 返回a//b 完全变复杂了，我还不如直接写 a//b

#11. index( a) 返回a转为整数的结果

#12. inv( obj) 按位取反  对比 ~运算符

#13. lshift(a,b) a左移b位

#14. mod( a, b) 返回 a%b 余数

#15. mul(a, b) 如果a,b是数字，返回 a*b multiple


#16. matmul( a,b) 返回 a@b 矩阵乘法 matrix multiple
#print( [[1,2],[3,4]]@[[1,2],[3,4]] ) #这个报错了，因为类型是list
#import array 内置数据类型自带的array，但是仍然需要引入
#print( array.array('d',[[1,2],[3,4]])@array.array('d', [[1,2],[3,4]]) ) #这个报错了，因为类型是list#报错，必须是一个real number，不能是list

from numpy import array
print( array([[1,2],[3,4]])@array( [[1,2],[3,4]]) ) #这个成功了

#17. operator.neg( obj)

#18. or_( a, b) #按位或

#19. pos( obj) 返回obj取正的结果

#20. pow( a, b) #a,b要是数字的话，返回 a**b

#21. rshift(a,b)

#22. sub( a,b) 返回 a-b

#23. truediv( a,b) 真除法，返回 a/b 比如 2/3=0.66

#24. xor( a,b) 返回 a^b 异或

#25. concat( a,b) 对于序列a,b返回 a+b
import operator
print( operator.concat( [1,2,3], [2,3,4])) #类比list的 extend()

#26. contains( a,b)  # b in a 检测的结果，注意操作数是反序的 是 b in a，
print( operator.contains([1,2,3], 1))

#27. countOf( a, b) 返回 b在a中出现的次数

#28. delitem( a, b) #移除a中索引号为b的值，返回值为空?

#29. indexOf(a, b)

#30. setitem(a, b, c)

#31. length_hint( obj, default=0) #实际长度，估计长度， 默认值。优先级从高到低

#32. call(obj, /, *args, **kwargs) #必须是可调用对象

#33. operator.attrgetter( attr)

#34. itemgetter( *items)

#35. methodcaller( name, /, *args, **kwargs)
