
#原地运算，就是不消耗额外的空间 ?是的， 修改变量而不需要消耗额外的空间

#1.iadd( a, b) #等于 a +=b  inplace add
'''源代码如下 github中的cpython项目
def iadd( a, b):
    a += b
    return a
'''


#2. iand( a, b) # 等价于 a &=b

#3. iconcat( a, b)
'''
def iconcat( a, b):
    if not hasattr( a, '__getitem__'):
        msg="'%s' object can't be concatneated % type(a).__name__
        raise TypeError( msg)
    a +=b
    return a
'''
import operator
print( operator.iconcat( [1,2,3], [4,5]))  #和extend()方法很像，这几行代码怎么做到的
#我知道了，因为 [1,2,3]+[4,5] ==[1,2,3,4,5]
print( [1,3,4]+[6,8,2])

#4. ifoloordiv( a,b) #== a //=b

#5. ilshift( a, b) # == a << b

#6. imod( a, b) # == a%=b

#7. imul( a, b) # a*=b

#8. imatmul( a, b)  # a@=b

#9. ior( a, b) # a|=b

#10. ipow(a, b) # a**= b

#11. irshift(a, b)

#12. isub(a,b) # a -=b

#13. itruediv( a, b)  # a/=b

#14. ixor( a, b) # a ^=b
