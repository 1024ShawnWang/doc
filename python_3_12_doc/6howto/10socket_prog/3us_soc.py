
###############使用一个套接字

#1. 客户端套接字和服务器端套接字极其相似，都是点对点的

#2. 两组用来通信的方法，send和recv。
#2.1 改动 客户端套接字 到文件类型，也可以使用 read 和 write
#2.2 wirte()完毕，记得 调用 flush()方法，来确保网络缓冲可以写入

#3. send 和 recv 操作网络缓冲区，网络缓冲区清空时候，两个方法返回。告诉你处理了多少字节
#网络缓冲区， 在自己机器上等待发出的数据包，根据网络协议，全部发出之前数量可能会变化，所以有的时候不会立刻全部发出
#3.1 recv方法返回0字节的时候，就表示另一端已经关闭了连接，你就再也不能从这个连接获得信息了；但是你可以发送

#4.http协议，只是使用 一个套接字，进行一次传输。 客户端发起一个请求，然后读取响应，然后销毁
#4.1 补充 tcp三次握手
#b我不准备补充，如果没有封装的意识，知识恐怕能学到死

#5. 套接字里面不存在 abbr:EOT 传输结束的。send或者recv 只要发送了0字节，就会导致连接中断
#5.1 因为套接字无法告诉你，不要再读取了。因此，必须设计一个返回值，使得连接被中断，否则连接就会一直保持了
#5.2 因此，你发送的消息，必须必须有如下之一的特点，1.固定长度，2.可以在发送内部被确定，3.关闭连接的时候就可以结束

#5.3 如果你不希望结束连接，最简单的办法就是使用第一个办法，使用固定长度的消息
#例子如下:
class MySocket:
    def __init__( self, sock=None):
        if sock is None:#如果没有，那就新建一个
            self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock #绑定到实例上

    def connect( self, host, port):
        self.sock.connect( (host, port))

    def mysend( self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send( msg[ totalsent:] ) # send( msg[0:]，返回发送出去的字节数)
            if sent == 0:
                raise RuntimeError('socket connection broken')
            totalsent = totalsent + sent
    
    def myreceive( self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv( min(MSGLEN - bytes_recd, 2048)) #socket.recv( bufsize[, flag]) bufsize就是一次性最大接受的数据长度（字节);返回值是代表数据的字节流对象
            if chunk == b'':
                raise RuntimeError( 'socket connection broken')
            chunks.append( chunk)
            bytes_recd = bytes_recd + len( chunk) #移动磁头到下一个连续的读取点
        return b''.join( chunks)

#MSGLEN是什么呢？
#就是 msg的长度，mysend( msg)方法中，可以理解为 len( msg)
#但是 myreceive( )中，不知道怎么办，因为根本就不知道对象是什么，更别说长度了，只知道是字节流

#5.3.1 发送部分代码确实可以用于传送任何消息
#5.3.2 接收的代码，可以用第一个字符来表示消息对象的类型，由类型来决定长度。这样，需要两次recv，第一个取得第一个字符，来获得长度，第二次在循环中获取剩余的所有消息；或者决定分界符，之后扫描整个对象来分割消息

#6. 如果你的会话协议允许多个消息被发回来，（即使在没有响应情况下），调用recv传入任意大小的块，你可能会因为读到后续接收的消息而停止读取
#你需要一边放到一边保存，直到需要它为止
#后面都看不懂了


################################
#二进制数据
#1. 可以通过套接字发送二进制数据，主要问题是，不同的数据会按照不同格式读取二进制数据
#2. 网络字节顺序是大端序的，所谓大端序：最大的字节在前，一个值为1 的十六位整数，将会按照如下顺序发送 00 01
#3. 但是cpu是小端序的，所谓小端序：最小的字节在前，同样的1，表现为 01 00

#4. Socket库中，有转换16位，和32位的调用 ntohl, htonl, nths, htons, 其中 n表示 网络， h表示主机， s表示 short ，l表示long。
#4.1 当网络顺序 与 主机顺序相同时，这些调用不做任何事情，当相反的时候，这些调用适当地交换字节
