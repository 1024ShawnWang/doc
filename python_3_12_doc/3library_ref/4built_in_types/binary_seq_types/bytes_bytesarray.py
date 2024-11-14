
#1. b开头的对象，表示这是一个bbytes对象

#2. class bytes( [source, [encodig, [, errors] ] ] )

#3. classmethod formhex( string)    从十六进制直接转换为字节对象，具体用法还是没搞清楚，  '.'在utf-8 和ascii中是46，十六进制写作\0x2e=2*16+14

#4. unicode编码和utf-8编码: unicode是字符集， 收录了世界上所有图像，并且给了一个唯一的数值，或者叫码点
                         #: utf-8   是更具体的编码规则，声明了如何在计算机里存储这些数值， utf-8是变长的，1-4个字节

#5. hex( [sep [ bytes_per_sep] ] ), 返回一个字符串对象

#6. bytes是不可变对象


#bytesarray

#1.为了突破bytes不可变，创造的类

#2. class bytesarray( [source, [, encoding [, errors] ] ] )

#3. classmethod fromhex( string)

#4. hex( [sep[, bytes_per_sep] ] )
