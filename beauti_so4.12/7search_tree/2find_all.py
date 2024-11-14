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
import re

soup = BeautifulSoup( html_doc, 'html.parser')
#1. find_all( name, attrs, recursive, string, **kwargs)

#2. find_all会搜索当前tag的所有子节点，可以传入一个过滤器

#3. name是tag的namg，自然地所有字符串都会被忽略，毕竟它们是NavigableString对象
print( soup.find_all("title") ) #[<title>The Dormouse's story</title>]
#3.1 name的参数值有 3.1.1字符串，3.1.2正则表达式， 3.1.3列表， 3.1.4方法， 3.1.5True

######################################################################################
#4.关键字参数
print( soup.find_all( id="link2") )#4.1 值是字符串

print( soup.find_all( href=re.compile("elsie")) ) #4.2值可以是正则表达式

#4.3可以是列表
#4.4可以是方法
#4.5可以是True

print( soup.find_all( href=re.compile("elsie"), id="link1")) #5. 使用多个k-v，来多重过滤

data_soup=BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
#print( data_soup.find_all( data-foo="value") ) #6.有些属性无法被取得，比如html5中的 data-*属性
print( data_soup.find_all( attrs={'data-foo':'value'})  )#6.1但是可以使用attrs={k:v}传入一个字典，来获得

name_soup = BeautifulSoup('<input name="email"/>', 'html.parser')
print( name_soup.find_all(name="email")) #7.当name出现在attrs中时候，使用k-v是搜索不到的
print( name_soup.find_all( attrs={"name":"email"} )) #7.1使用关键字参数attrs来强调name是attr中的key，而不是tag名称


######################################################################################
#按css搜索
print( soup.find_all( "a", class_="sister") ) #1. classs可以是属性，但是与python保留字冲突，所以使用了class_ (注意下划线

print( soup.find_all( class_=re.compile("itl")) )#2. class_仍然接受过滤器：字符串，正则表达式，列表，方法，True

def has_six_characters( css_class):
    return css_class is not None and len( css_class)==6
print( soup.find_all( class_=has_six_characters) ) #2.1关键字参数传入方法

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
css_soup.find_all("p", class_="strikeout") # [<p class="body strikeout"></p>] #3.class是多值属性，按照一部分都可以搜索到
css_soup.find_all("p", class_="body")# [<p class="body strikeout"></p>]

print( css_soup.find_all( "p", class_="body strikeout")) #4.也可以传入多个单词（多值），但是顺序要完全一致，否搜索不到
print( css_soup.find_all( "p", class_="strikeout body")) #

print( css_soup.select( "p.strikeout.body"))  #5. 使用css选择器来专门对class进行筛选
print( css_soup.select( "p.body.strikeout"))  #5.1 css选择器对比4，这个是可以顺序混乱的


######################################################################################
#string参数
#1. string参数是专门对NavigableString对象进行过滤的，类比attrs对tag，但是有不同肯定

#2. 接受 字符串，正则表达式，列表，方法，True
print( soup.find_all( string="Elsie") ) #2.1字符串  （完全匹配
print( soup.find_all( string=["Tillie", "Elsie", "Lacie"]) )#2.2列表 （完全匹配
print( soup.find_all( string=re.compile("Dormouse"))) #2.3正则，这里面是包含匹配
def is_the_only_string_within_a_tag( s):
    """return True if and only if this string is the only child of its parent tag"""
    return (s==s.parent.string)
print( soup.find_all( string=is_the_only_string_within_a_tag))

print( soup.find_all("a", string="Elsie") )#3. string是标签中间的字符


#####################################################################################
#limit参数
print( soup.find_all( "a", limit=2)) #1.限制搜索数量 <=2此时
#[ <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

####################################################################################
#recursive参数：禁止递归搜索，只搜索子节点，孙节点是想也不要想
print( soup.html.find_all( "title") ) #<title>...</title> #1.默认使用递归搜索
print( soup.html.find_all("title", recursive=False) ) #[] #2.只在子节点搜索 


####################################################################################
#1. BeautifulSoup对象和 Tag对象，都可以使用 find_all()
