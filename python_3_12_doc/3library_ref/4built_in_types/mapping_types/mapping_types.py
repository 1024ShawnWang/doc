
#1.仅有一种标准类型dict

#2.dict的键几乎可以是任何值，但是要可变对象不可以，比如list, set

a ={'jack':490, 'tock':32} #3.  花括号+冒号+逗号； 字典推导式； 类型构造器
#d ={b:c for b in range(3) for c in range(3)}
d={x:x**2 for x in range(4)}#推导式要求可以用一个变量表达key-val，或者key- value必须满足某个函数关系
e= dict(one=1, two=2, three=3)#用的是() ; key的类型会变成str
print( e)


print( list( e) ) #4. 返回所有key的列表

print( len(e) ) #5.项的个数

print( e['one'] )  #6.索引，注意是字符串

e['one']=11      #7.设置

#8. in

#9. not 

print( iter(e) ) #10返回一个迭代器，key组成的

e.clear()  #11.移除所有内容

#12. copy()

#13. classmethod fromkeys( iterable, value=None, /)  使用iterable作为key，val全部为None
l=[1,2,3]
l=dict.fromkeys( l) 
print( l)


#14.get(key, default=None) 安全取办法，不存在的时候就返回None

print( l.items() )#15.返回一个视图对象

#16.pop()

#17.popitem()

print( reversed( l)) #迭代器对象，返回一个逆序key.  reversed居然也成了关键字，我们没加任何前缀

k={1:1, 2:2, 3:3, 4:4}
l.update( k)         #19. update办法，key和val都会更新
print(l )

print('*****')
o={1:4}
n =l | o      #20. | 运算符，合并两个字典，返回一个新字典，后者优先级高
print( n)

l |= o     #21用o更新了， 完全等于上面的操作，此时l==n
print( l)
