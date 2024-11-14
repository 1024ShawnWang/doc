def scope_test():
    def do_local():
        spam='local spam'

    def do_nonlocal():
        nonlocal spam
        spam='nonlocal spam'

    def do_global():
        global spam 
        spam ='global spam'

    #spam是在方法内定义的变量
    spam ="test spam"
    do_local()
    print('after local assignment: ', spam)

    do_nonlocal()
    print('after nonlocal assignment: ', spam)

    do_global()
    print('after global assignment: ', spam)


#调用最外层的办法
scope_test()
print('In global scope: ', spam)


'''
scope是textual region of python program where namespace is directly accessible

我觉得有更好的理解，就是和谁对齐，对齐的语句会共用一个命名空间  
就是 到***最左边****的距离(空格/tab数量 

调用函数时候 就是被调用函数在此行，此列执行，拥有的变量，自然变成下个scope的变量(就是局部变量

'''

'''
scope有四个层次：(搜索优先级从高到低
1.the innermost scope,最先搜索，包含所有的局部变量的全称
2.scopes of any enclosing functions,包含所有既不是局部变量，又不是全局变量的所有变量的全称
3.next-to-last scope : 包含目前模块所有的全局变量名称(独一无二的全称)
4.the outermost scope( search last)(最后搜索的，是所有内置函数的命名空间)
'''
#1. nonlocal 将最内侧变量，前进一个命名空间

#2. global 将变量移到最左边的命名空间

#3. 最内层的变量如果不使用nonlocal声明的话，只能读取，并不能被写
#    这相当于父类对象，肯定不可以直接改变 子类对象的属性， 最多可以读取。
#   但是继承了父类的属性，子类声明nonlocal就可以改变父类的属性

#4. 语句使用的变量，自己就是自己所属的scope的变量的值,比如这里的print

#5. 所以python把变量分为了三类：全局的(next_to_last scope)，局部的(innermost scope)（最内层的变量），其他变量。是这么个逻辑
