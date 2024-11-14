
#1.根据系统以及构建选项，此模块提供了各种套接字协议镞

#2.特定的 套接字对象 需要的地址格式 将 根据 此套接字对象 被创建时b指定的地址族 被 自动选。套接字 地址表示 如下：
#1 一个绑定在 文件系统节点上的 AF_UNIX 套接字的地址 表示为一个字符串

#2 (host, port)被用作 AF_INET地址族。 host是 一个表示互联网域名标记的主机名称（例如 'daring.cwi.nl'或者IPV4地址（例如 4.4.4.4）。 port是一个整数

#3 对于 AF_INET6地址族，使用一个四元组(host, port, flowinfo, scope_id)

#4. AF_NETLINK 套接字由一对(pid, groups)表示

#5. 指定AF_TIPC地址族可以使用 仅Linux支持的 TCP协议 (addr_type, v1, v2, v3[, scope])

#6. AF_CAN 地址族使用元组( interface, )其中interface是表示网路接口名称的字符串，如eth0。网络接口名 '' 可以用于接收本族所有网络接口的数据包

#7. PF_SYSTEM

#8. AF_BLUTETOOTH支持以下协议和地址格式 （好家伙，合着还可以蓝牙通信呢）
#8.1 BTPROTO_L2CAP 接收 (bdaddr, psm)，其中bdaddr 为字符串格式的蓝牙地址，psm是一个整数
#8.2 BTPROTO_RFCOMM 接收(bdaddr, channel) channel是一个整数
#8.3 BTPROTO_HCI接收(device_id) 其中device_id为整数或者字符串，它表示接口对应的y蓝牙地址
38.4 BTPROTO_SCO 接收 bdaddr， 其中 bdaddr是 bytes 对象，其中含有字符串格式的蓝牙地址如 b'12:23:34:45:56:67'

#9. AF_ALG 是一个仅 Linux 可用的，基于套接字的接口，用于连接内核加密的算法。算法套接字可用包括2到4个元素的元素来配置 (type, name [, feat [, mask]])，其中
#9.1 type是表示算法类型的字符串，如 aead, hash, sccipher 或者 rng
#9.2 name是表示算法类型和操作模式的字符串，如 sha256, hmac(sha256), cbc(aes)
#9.3 feat 和 mask 是 无符号的32位整数

#10. AF_VSOCK用于支持虚拟机与宿主机之间的通讯。该套接字用( CID, port)元组表示，都是整数

#11. AF_PACKET 是一个直接连接网络设备的低层级接口。 地址以元组 （ ifname, proto[, pkttype[, hatype[, addr]]])，其中
#11.1 ifname 指定w设备名称的字符串
#11.2 proto 以太网协议号
#11.3 pkttype #11.3.1PACKET_HOST(默认) #11.3.2 PACKET_BROADCASE物理层广播的数据包 #11.3.4 PACKET_MULTICASE #PACKET_OTHERHOST
#11.4 hatype 可选整数， 指定ARP硬件地址类型
#11.5 addr 可选

#12. AF_QIPCRTP 是一个仅 Linux 可用的， 基于套接字的接口

#13. IPPROTO_UDPLITE 是一个UDP变体，允许指定数据包的哪一部分 计算入 校验码

#14. AF_HYPERY windows专属的，用于同Hyper-V主机的客户机通信的，基于套接字的接口

#15.
