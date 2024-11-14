
fruits=['orange','apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

#df 
print( fruits.count('apple'))
print( fruits.count('tangerine'))
print( fruits.count('apple'))
print( fruits.index('banana', 4))

#返回值是零,错了，返回值是None
print( fruits.reverse() )

#打印fruits
print( fruits)


fruits.append('grape')
print( fruits)

fruits.sort()
print( fruits)

#
print( fruits.pop() )


'''总结，
insert, remove, sort 几个办法的返回值都是None.


这在所有***可变数据类型****都如此设计，
'''


