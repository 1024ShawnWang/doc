from bs4 import BeautifulSoup

#1. class bs4.element.NavigableString 可遍历的字符串。这个对象是 **tag中文本** 的抽象

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print( tag.string) # 'Extremely bold'
print( type(tag.string)) # <class 'bs4.element.NavigableString'>

unicode_string = str( tag.string) #2.使用 str将 NavigableString对象转为 str对象
print( unicode_string)
print( type( unicode_string)) # <class 'str'>

tag.string.replace_with( 'No longer bold') #3. 使用 replace_with()修改文本内容
print( tag)

#4. NS对象 支持 遍历文档树 和 搜索文档树 大部分属性，并非全部。 
#4.1 它无法包含其他内容， 不支持 .contents, .string 或者 find方法

#5. BeautifulSoup之外使用 NS对象？？？
