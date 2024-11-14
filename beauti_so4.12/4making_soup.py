from bs4 import BeautifulSoup

'''
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
'''

1.如上，传入一个句柄或者字符串，返回一个beautifulsoup对象

2. 它会先被转为unicode,如果没有'html.parser'，bs会选择最合适的解析器来解析它
