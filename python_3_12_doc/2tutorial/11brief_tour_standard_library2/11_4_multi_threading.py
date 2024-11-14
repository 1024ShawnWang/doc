#异步压缩指定文件（其实就是后台执行)
#什么叫异步呢？(后台？)
import threading, zipfile #1.zipfile 读写zip文件

class AsyncZip( threading.Thread):#继承Thread
    def __init__( self, infile, outfile):
        threading.Thread.__init__( self)
        self.infile =infile
        self.outfile =outfile

    def run( self):
        f =zipfile.ZipFile( self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write( self.infile)
        f.close()
        print("Finished background zip of : ", self.infile)


background =AsyncZip('mydata.txt', 'myarchive.zip')
background.start() #2.线程如何开始

print("主要程序在前台运行中....")

background.join() #3.如何在主程序存在期间，等待异步线程结束，确保它能完成自己的目标
print("主要程序结束")

#4.主要困难来自于异步读写，python提供了线程锁等模块，来解决这个问题

#5.对于较小的项目，使用queue模块来解决异步线程读写的问题
