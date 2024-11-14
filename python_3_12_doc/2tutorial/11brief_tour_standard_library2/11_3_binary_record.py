import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start=0

for i in range(3): #show the first 3 file headers
    start +=14
    fields =struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size =fields

    start +=16
    filename = data[ start: start+filenamesize]

    start +=filenamesize
    extra = data[ start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size #跳到下一个开头


#完全看不懂思密达
#struct好像是网络编程里面有的，struct也许可以
#卧槽牛逼真的读取出来了，myfile其实是v2ray的安装包压缩文件
