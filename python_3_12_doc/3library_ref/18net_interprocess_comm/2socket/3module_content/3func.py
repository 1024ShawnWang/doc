
##下面是如何创建 套接字对象
#1. class socket.socket( family=AF_INET, type=SOCK_STEAM, proto=0, fileno=None) 使用给定的地址族，套接字类型和协议号 创建一个 新的 套接字
#1.1 family应该为 AF_INET(默认值), AF_INET6, AF_UNIX, AF_CAN, AF_PACKET, AF_RDS 其中之一
#1.2 type应该为 SOCK_STREAM(默认值), SOCK_DGRAM, SOCK_RAW, 或者其他可能的 SOCK_ 常量之一
#1.3 protoy通常为0，也可以省略。当family=AF_CAN情况下， proto应该为 CAN_RAW, CAN_BCM, CAN_ISOTP, CAN_J1939
#1.4 如果指定了fileno, 那么将从指定的文件描述符中检测 family, type, 和 proto的值

#2. 新建的套接字 不可继承

#3. socket.socketpair( [family[, type[, proto]]] )对比1，但这个创建一对已连接的套接字对象

#4. socket.create_connection( address, timeout=GLOBAL_DEFAULT, source_address=None, *, all_errors=False)
#连接到一个互联网 address （ 用 (host, port)二元组表示）上侦听的 TCP 服务，并返回套接字对象

#5. socket.create_server( address, *, family=AF_INET, backlog=None, reuse_port=False, dualstack_ipv6=False)
#d创建绑定到 address的 TCP 套接字，并返回该套接字对象 的 便捷函数

#6. socket.has_dualstack_ipv6() 如果平台支持创建 IPv4和 IPv6连接都可以处理的 TCP 套接字

#7. socket.fromfd( fd, family, type, proto=0)

#8. socket.fromshare( data)

#9. socket.SocketType 这是一个python对象类型， 等同于 type( socket(...))

##其他功能
#1. socket.close( fd) #关闭一个 套接字文件描述符

#2. socket.getaddrinfo( host, port, family=0, type=0, proto=0, flags=0)
import socket
print( socket.getaddrinfo( 'example.org', 80, proto=socket.IPPROTO_TCP) )

#3. socket.getfqdn( [name] ) 返回name的完整限定域名

#4. socket.gethostbyname( hostname) 将主机名转为ipv4地址格式

#5. socket.getthostbyname_ex( hostname) 

#6. socket.gethostname() 返回一个字符串，包含当前正在运行python解释器的机器的主机名
print( socket.gethostname()) #Tutu

#7. socket.gethostbyaddr( ip_address)

#8. socket.getnameinfo( sockaddr, flags)

#9. socket.getprotobyname( protocolname) #将一个互联网协议名称转w写为 能被作为 第三个参数传给 socket()函数的常量

#10. socket.getservbyname( servicename[, protocolname]) 将一个互联网服务名称和协议名称 转为 该服务的端口号

#11. socket.getservbyprot( port[, protocolname])

#12. socket.ntohl( x) #将一个32位正整数 从网络字节序， 转换为 主机 字节序

#13. socket.ntohs( x) #将一个16位正整数。。。。

#14. socket.htonl( x) #

#15. socket.htons( x)

#16. socket.inet_aton( ip_string) 将ipv4地址，以点号分为四段的字符串格式

#17. socket.inet)ntoa( packed_ip)

#18. socket.inet_pton( address_family, ip_string)

#19. socket.inet_ntop( address_family, packed_ip )

#20. socket.CMSG_LEN( length)

#21. socket.CMSG_SPACE( length)

#22.下面的也略过了，不知道有啥意义
