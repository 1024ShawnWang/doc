import reprlib #1. provides versions of repr()
s =reprlib.repr( set('supersdfsdfdsfsdlnmbfowqzdshfbhdshsdsfgj') )
print( s)

import pprint  #2.pprint for pretty printer可以更加精细地控制输出
t=[[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 
    'yellow'], 'blue']]]
pprint.pprint( t, width=30)
print( t) #作为对比

import textwrap #3.美化文本输出
doc ="""The wrap() method is just like fill() except that it returns a list of string instead of one big string with newline to separate the 
wrapped lines"""
print( textwrap.fill( doc, width=40))

#4.还有locale，也是美化的作用好像，不看了思密达
