#在Linux命令行 使用python模块，解析 json，如下
#echo '{"json":"obj"}' | python -m json.tool


#但是直接作为脚本文件执行，却显示找不到python
#!/usr/bin/bash
echo '{"json":"obj"}' | python -m json.tool
