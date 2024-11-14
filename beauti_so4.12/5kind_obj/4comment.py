from bs4 import BeautifulSoup

#1. 前面三个对象基本覆盖了全部文档内容，但是还有文档注释没有被表示

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print( type(comment) )# <class 'bs4.element.Comment'>

#2. Comment对象是一个 特殊的 NavigableString对象
print( comment)


############注意，下面全是 NavigableString的子类，而不是 Comment
#3.对于HTML
#3.1 class bs4.Stylesheet 表示嵌入的 css 脚本；内容是<style>标签内部的所有字符串
#3.2 class bs4.Script 表示嵌入的JavaScript脚本；内容是 <script>标签内部的所有字符串
#3.3 class bs4.Template 表示嵌入的 HTML模板，内容是 <template>标签内部的所有字符串

#4.对于XML文档
#4.1 class.bs4.Declaration 表示XML文档开头的 declaration
#4.2 class.bs4.Doctype 表示可能出现在XML文档开头的 document type declaration
#4.3 class.bs4.CData 表示 CData section
#4.4 class.bs4.ProcessingInstruction 表示 XML处理指令
