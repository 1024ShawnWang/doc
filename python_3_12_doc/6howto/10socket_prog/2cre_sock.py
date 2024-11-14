
#1. 创建套接字
#1.1 如何创建一个客户端套接字
'''
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM) #创建一个 INET, STREAMING 套接字. socket.SOCK_STREAM还有其他值， 比如 SOCK_DGRAM, SOCK_RAW
s.connect( 'www.python.org', 80) #连接到 服务器80端口
'''
#1.2 连接完成，套接字就可以用来发送请求， 来接收页面上显示的文字
#1.3 这个套接字也会用来读取响应
#1.4 之后，被销毁。一个客户端套接字通常 用来做一次交换(请求，响应)


#2.1.此时，服务器套接字：
'''
seversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) #创建一个 INET, STREAM套接字

serversocket.bind( socket.gethostname(), 80) #将套接字绑定到一个全局的主机和接口  #gethostname()将返回一个字符串，包含当前正在运行此pyhon解释器的机器的 主机名称

serversocket.listen( 5) #称为服务器套接字
'''
#

#2.2 使用了 socket.gethostname()，所以套接字将外网可见

#2.3 如果使用 s.bind( 'localhost', 80) 或者 s.bind( '127.0.0.1', 80)，这个套接字只会在同一台机器上的套接字程序可见

#2.4 如果使用 s.bind( '', 80)，则指定套接字可以被机器上的任何地址 连接？？？

#2.5 低端口号通过被占用，最好使用高端口，4位及以上的数字

#2.6 listen( 5) 的参数 5， 会告诉套接字库，我们希望队列中累积最多5个的连接请求，再拒绝外部连接。

#3. 我们现在已经有了一个【服务端】 套接字，监听了 80 端口，现在进入网络服务器的主循环。我把前面的代码也抄上
'''
seversocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM ) 
serversocket.bind( socket.gethostname(), 80) 
serversocket.listen( 5) #称为服务器套接字

while True:
    (clientsocket, address) = serversocket.accept() #接受外来的连接
    #执行一些对 clientsocket的操作
    #ct = client_thread( clientsocket)
    #ct.run()

#3.1 通常有三种办法可以让这个循环工作起来，
#3.1.1 调度一个线程
#3.1.2 把这个应用改成非阻塞模式套接字，亦或使用 select库来实现【服务器】套接字
#3.1.3 第三种办法呢？

#3.2 最重要的理解： 一个服务器 套接字，它并没有发送任何数据，没有接受任何数据。它只创建 【客户端】套接字

$3.3 每个【客户端】套接字，都是为了响应 某些其他客户端套接字 connect()到我们绑定的主机

#3.4 一旦创建【客户端套接字】完成，就会返回，并监听更多的连接请求。 看到了把，什么时候开始继续处理 listen呢，就是创建 客户端套接字完成的时候， 就是服务器的 accept， 和客户端的connect

#4. 

##########################################################################
##########################################################################
#进程通信
#1.使用套接字进行 进程通信

#2.复习四层模型
'''
    应用层      python应用程序
    传输层      tcp/udp
    网络层      ip
    链路层      mac
'''
#3.socket编程，就接受应用层命令，向传输层发送命令， python提供的进程 multiprocessing模块的进程通信，应该在应用层？

##################################
#1. 同一台机器，进行ipc，应该考虑 管道或者 共享内存
#2. 也可以使用 AF_INET类型的套接字，绑定【服务端】套接字到 'localhost'上，大多数平台上，这会使用网络层的快捷方式（本地回环），速度比大多数网路通信要快太多太多

#3. 

