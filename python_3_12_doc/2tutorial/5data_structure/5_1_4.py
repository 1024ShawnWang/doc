
#nested list Comprehensions

matrix =[
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]


#1.使用列表生成式transpose矩阵
a=[ [row[i] for row in matrix]  for i in range(4)]
print( a)

#2.按照列表生成式=[] + append()，重写一下这个方法
k1=[]
for i  in range( 4): #注意先写的是for循环，因为[row[i] for row in matrix]带了中括号，是个元素
    k1.append( [row[i] for row in matrix] )
print( k1)
#看不清的话，可以再扩写一下 [row[i] for row in matrix]


#3.矩阵的转置有专门的函数
print( list( zip(*matrix)) )
