
#1.用户可以自定义异常,通过继承某些异常类

'''
try:
    raise KeyboardInterrupt
finally: #2.使用finally关键字，进行 clean-up ，无论如何都要执行的操作
    print('无论如何，都要再见')
'''

def divide( x, y):
    try:
        result =x/y
    except ZeroDivisionError:
        print('分母为0了')
    else:
        print('结果是 ', result)
    finally:
        print('执行了finally语句')

#finally语句总会执行，所以特别适合关闭文件或者连接，无论是否打开成功，用来释放内存

#3. 使用with语句，可以自动省略finally: close()的过程，是一个封装。
