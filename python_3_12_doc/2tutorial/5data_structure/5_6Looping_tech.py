
knights ={'gallahad':'the pure', 'robin':'the brave'}

for k, v in knights.items(): #1. items()是一对
    print(k, v)


for i, v in enumerate( ['tic', 'tac', 'toe'] ): #2. enumerate()可以给序列对象一个下标( sequence object)
    print(i, v)

questions=['name', 'quest', 'favorite color']
answers =['lancelot', 'the holy grail', 'blue']
for q, a in zip( questions, answers): #3. zip()方法可以将两个对象组成一对，类似于items()方法，
    print( 'What is your {0}? It is {1}.'.format(q,a) )

for i in reversed( range(1, 10, 2)): #4. 反向遍历
    print( i)

basket=['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted( basket): #5. sorted()会返回一个排序的列表（既然返回非空，那么肯定就不会改变原来列表的结构了
    print(i)


for f in sorted( set( basket)): #6. 使用set来唯一地遍历列表
    print( f)


#7. 如果边循环边修改结构，最快速和安全的做法是遍历复制品，修改源品
