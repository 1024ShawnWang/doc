html_doc = """<html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>

    <p class="story">...</p>
"""
######关于这个文档，提醒两点，1. 缺失了</body>和 </html>并没有影响解析 2.开头"""之后不能换行，否则影响 len( soup.contents)的元素数量，会加进入一个换行符 '\n'

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

#1. tag 可以包含多个字符和其他tag，但是字符串不行，因为它是 navigablestring对象，不能包含其他对象

print( soup.head) #2. 直接使用tag name这个属性，直接找到发现的第一个tag，name就是<下面紧接着的字符串

soup.find_all( 'a') #3. 使用 find_all方法，传入 名称字符串，返回一个列表

#####################################################
##########.contents 和 .children
#1. Tag的 .contents属性 可以将 tag的全部子节点 以列表的s形式返回
head_tag = soup.head
print( head_tag)    # [<head><title>The Dormouse's story</title></head>]

print( head_tag.contents) #<title>The Dormouse's story</title> #2. .contents输出内容不会包含自身

print( head_tag.contents[0].contents) #The Dormouse's story #3.返回的是列表，所以要用索引操作符

print( len( soup.contents)) #1 #4.BeautifulSoup第一个标签 <html></html>包围了整个文档

print( soup.contents[0].name) # 'html'

#5. 字符串没有 .contents内容，已经说过很多次了，因为它没法包含其他内容

title_tag = head_tag.contents[0] #<title>The Dormouse's story</title>
for child in title_tag.children: #6. .children返回一个迭代器
    print( child) # 'The Dormouse's story #只有这一个子节点

#7. 想要修改tag的子节点，要使用 修改文档树 的办法，不要直接修改 contents中的列表，会导致细微且难以定位的问题


###############################################################################
###################### .descendants
#1. .contents和 .children 属性，仅仅包含 tag的直接子节点   #只进入到下面一层的文件夹

#2. 对比1，.descentdants属性， 可以对所有tag的子孙节点进行递归循环 #深度搜索，进入到最后无法搜索的navigablestring节点

for child in head_tag.descendants: #head_tag=<head><title>The Dormouse's story</title></head>
    print( child)
#<title>The Dormouse's story</title>
#The Dormouse's story
#可以看到将两个对象都输出了


#######################################################################################
############ .string
#1. 如果 tag 只有一个 NavigableString子节点，那么这个tag可以使用 .string 属性得到子节点
print( title_tag.string) #title_tag =<title>The Dormouse's story</title>，将输出 'The.. story'

#2. 如果tag只有一个子节点，也可以使用 .string办法获得这个子节点

#3. 如果有多个子节点，返回None


######################################################################################
######### .strings 和 stripped_strings
#1. strings 可以获取 tag内的所有字符串
for string in soup.strings:
    print( repr( string))

#2. 可以使用 .stripped_strings来去除多余h空白内容，比如上面的换行符
for string in soup.stripped_strings:
    print( repr(string))
