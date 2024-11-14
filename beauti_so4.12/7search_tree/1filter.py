html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')


#1. 过滤器可以作用在 tag 的 name上，节点的属性上，字符串上，或者与它们混用
    
print( soup.find_all('b') ) #1.1 直接传入节点 name的字符串
#1.2 如果传入字节码参数，会被当作utf-8编码

import re
for tag in soup.find_all( re.compile("^b")): #2.仍然是对name进行过滤，调用的是正则表达式的match()方法
    print( tag.name) #这里面是必须以t开头

for tag in soup.find_all( re.compile("t")):
    print( tag.name) #将输出html和title ，这两个tag的name里面都含 t


print( soup.find_all( ["a","b"])) #3. 如果传入列表，会被认为是 或运算
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


for tag in soup.find_all( True): #4. True值匹配所有tag对象，但是不包括NavigableString对象
    print( tag.name)


#################################################函数
print( soup.prettify())
def has_class_but_no_id( tag):
    return tag.has_attr("class") and not tag.has_attr("id")
print( soup.find_all(  has_class_but_no_id) ) #5. 传入函数的话，tag会被送入函数中，如果返回True，就会被选中
'''
 [<p class="title"><b>The Dormouse's story</b></p>,
  <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
  and they lived at the bottom of a well.</p>
  <p class="story">...</p>]
'''
# 这些都是 指定了 class 属性，但是没有id的 Tag ，注意看第二个，输出的是整个tag，即使内部的.contents不满足过滤器条件

def not_lacie( href_cont):
    return href_cont and not re.compile("lacie").search( href_cont) #6.1正则表达式里面的search函数。如果包含就返回True #6.2 and 运算符会将两边转为bool类型
#print( not_lacie('wlss'))

print( soup.find_all( href =not_lacie) )#7. 如果传入k-v对，或者说关键字参数，会将 href在html中对应的值，作为参数传入v中

############################################################上面的全都是 Tag对象，下面是NavigableString对象
print('############################################################')
print('############################################################')
from bs4 import  NavigableString
def surrounded_by_strings( tag):
    return ( isinstance( tag.next_element, NavigableString) and isinstance( tag.previous_element, NavigableString) )  #最外层的括号保证and先算

for tag in  soup.find_all( surrounded_by_strings):
    print( tag.name ) #多了一个body ，不知道为什么, next_element直接进入下一个元素中，类比 .contents[0]

#next_element还是没搞懂啊
#文档被解析成树状结构，next_element就是第一个被解 的 子节点，
'''
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
上面的第一个<p></p>标签的 next_element就是 "Once a time.... were"这个NavigableString
name就是节点名称，可以重复，闭合标签中间的值就相当于 节点的值， 这里就是 "Once.....were"
'''
print( soup.find("p", class_="story").next_element) #果然就是"Once...were"，不同于树状图的一点，节点值也会被解析（被认为最近的子节点
