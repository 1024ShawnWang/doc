#class pathlib.PurePath( *pathsegments) #1

#1.1 是windows风格和posix风格的 父类     

#2. class pathlib.PurePosixPath( *pathsegments)

#3. class pathlib.PureWindowsPath( *pathsegments)

#4. 无论你运行什么操作系统，都可以实例化这些类，因为它不会调用人任何操作系统操作（ 本质就是python按照各个系统，自己实现完了的办法）

#5. 相同风格的路径对象可以排序和比较

#6.  斜杠运算符可以帮助创造子路径

#7. PurePath.parts #可以访问路径中的各个部分

#8. 纯路径的 方法和属性

#1. PurePath.parser

#2. PurePath.driver

#3. PurePath.root 表示（局部或者全局） 根的字符串

#4. PurePath.anchor 驱动器和根的联合

#5. PurePath.parents

#6. parent

#7. name

#8. suffix

#9. suffixes

#10. stem

#11. as_posix()

#12. is_absolute()

#13. is_relative_to()

#14. is_reserved()

#15. joinpath( *pathsegments)
from pathlib import PurePosixPath
print( PurePosixPath('/etc').joinpath('passwd') )   

#16. full_match()

#17. match()

#18. with_name( name) 返回一个新路径，并修改name

#19. with_stem( stem) 返回一个带有修改后stem的新路径

#20. with_suffix( suffix) #返回一个新路径，并修改suffix

#21. with_segments( *pathsegments) 子类覆盖此办法，方便向派生路径传输信息
from pathlib import  PurePosixPath
class MyPath( PurePosixPath):
    def __init__(self, *pathsegments, session_id):
        super().__init__(*pathsegments)
        self.session_id =session_id

    def with_segments( self, *pathsegments):
        return type(self)(*pathsegments, session_id=self.session_id)

etc =MyPath('/etc', session_id=42)
hosts =etc/'hosts'
print( hosts.session_id)
