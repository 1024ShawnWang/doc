
basket={'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}#1.如何声明并且初始化，使用{} 保留字

print( basket) #2.集合的互异性

a = set( 'abracadabra')#3.使用set关键字，集合化一串字符串
b = set( 'alacazam')

print('******')
print( a)
print( b)
print('******')

print( a-b) #4.操作符-,意思显然地理解  a^(Cb) a和b补集的交

print( a|b) #5. aVb (并集)

print( a&b) #6.交集

print( a^b) #7. a并b -a交b，只在a或者只在b中的元素

c ={ x for x in 'abracadabra' if x not in 'abc'}#8. 同样使用生成式，注意花括号
print(c)


