
import zlib  #1. 信息压缩

s = b'witch which has witch watches wrist watch'#要压缩的信息 b for binary ,这样s是一个bytes对象，而不是string对象
print( len(s))

t=zlib.compress( s) #压缩
print( len(t))

print( zlib.decompress( t) ) #解压缩

