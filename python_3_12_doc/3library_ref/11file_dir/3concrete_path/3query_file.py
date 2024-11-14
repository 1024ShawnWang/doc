from pathlib import *

#1. Path.stat( *, follow_link=True)

#2. Path.lstat 同上，不同点在于返回（软链接）符号链接本身，而不是其信息

#3. Path.exists( *, follow_link=True)
print( Path('/').exists() )

#4. Path.is_file()

#5. Path.is_dir()

#6. Path.is_symlink()

#7. Paht.is_junction()  #只有windows支持 结合点

#8. Path.is_mount()  #是否是挂载点
p=Path('/dev/sda1')
print( p.is_mount()) #怎么输出了False?

#9. is_socket() 如果是一个 unix socket文件，就返回True

#10. is_fifo() #如果是个先进先出的设备

#11. is_block_device()

#12. is_char_device()

#13. samefile( other_path)

#14. samefile( other_path)
