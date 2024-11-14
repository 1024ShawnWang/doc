
while True:
    try:
        x = int( input("Please input a number : ") )
        break #如果能成功被int化，而且不抛出异常，就进入到break
    except ValueError: #1.如果抛出异常，就处理这一步
        print( "Oops! that was no valid number. Try again...")

#2.可以同时处理多个异常，except( RuntimeError, TypeError, NameError):

#3.多个except并列时候的顺序，下面的将依次打印B，C，D
'''
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
'''
#所以原则是按照 继承关系， 尽可能的传递给子类（因为子类更详细，处理的手段肯定比父类多)

