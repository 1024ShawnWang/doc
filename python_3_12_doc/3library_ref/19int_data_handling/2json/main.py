import json

l =json.dumps( ['foo', {'bar':('baz', None, 1.0, 2) } ]  )#解析json格式到python对象，返回一个str对象
print( l)
print( type(l))

print( json.dumps("\"foo\bar") ) #解析另一个json对象

print( json.dumps('\u1234'))

print( json.dumps('\\') )

print( json.dumps( {"c":0, "b":0, "a":0, }, sort_keys=True))

from io import  StringIO
io=StringIO()
json.dump( ['streaming API'], io)
print( io.getvalue())


#2. 指定分隔符，进行紧凑编码，注意比较两者的不同
print( json.dumps( [1,2,3,{'4':5, '6':7} ]  )  )
print( json.dumps( [1,2,3,{'4':5, '6':7}], separators=(',',':')) )
print( '******************************')

#3. 美化输出
print( json.dumps( {'6':7, '4':5}, sort_keys=True, indent=4) )


