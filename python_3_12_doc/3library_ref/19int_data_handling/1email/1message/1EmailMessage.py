#1. class email.message.EmailMessage( policy=default) 如果指定了 policy, 消息将由这个plicy所指定的规则 来更新和序列化信息的表达。 如果没有指定，那就是 default，这个策略遵循电子邮件的 RFC 标准，除了行终止符号（ RFC要求使用 \r\n，默认策略将使用 python标准的 \n 行终止符）

#2. as_string( unixfrom=False, maxheaderlen=None, policy=None) 以字符串形式返回 整个消息对象

#3. as_bytes

#4. __bytes__() 同上

#5. is_multipart() 如果该信息的载荷是一个 子EmailMessage对象列表，返回True，否则 False

#6. set_unixfrom( unixfrom)

#7. get_unixfrom() 返回消息的信封头

#8. __len__()返回标头的总数，包括重复项

#9. __contains__( name) 如果消息对象中 有一个名为 name的字段，则返回值为 True

#10. __getitem__( name)

#11. __setitem__( name, val)

#12. __delitem__( name) 对比9

#13. keys() 列表形式返回 消息头 中所欲的字段名

#14. values() 对比13，返回所有字段值

#15. items() 对比13,14

#16. get( name, failobj=None) 返回对应标头字段名的值

#17. get_all( name, failobj=None)

#18. add_header( _name, _value, **_params)

#19. replace_header( _name, _value) 对标头进行替换

#20. get_content_type() 返回消息的内容类型，

#21. get_content_maintype()

#22. get_content_subtype()

#23. get_default_type()

#24. set_default_type( ctype) 对比23看

#25. set_param( param, value, header='Content-Type', requote=True, charset=None, language='', replace=False) 

#26. del_param( param, header='Content-Type', requote=True)

#27. get_filename( failobj=None)

#28. get_boundary( failobj=None)

#29. set_boundary( boundary)

#30. get_content_charset( failojb=None)

#31. get_charsets( failobj=None)

#32. is_attachment()

#33. get_content_disposition()

#34. walk() 多功能生成器，深度优先遍历信息

#35. get_body( preferencelist=('related', 'html', 'plain')) 返回信息的MIME部分，这个部分最可能是信息体的部分

#37. iter_attachments() 

#38. iter_parts()

#39. get_content( *args, content_manager=None, **kw) #命名关键字参数

#40. set_content( 参数同上)

#41. make_related( boundary=None)

#42. make_alternative( boundary=None)

#43. make_mixed( boundary=None)

#44. add_related( *args, content_manager=None, **kw)

#45. add_alternative( *args, content_manager=None, **kw)

#46. add_attachment(参数同上）

#47. clear()

#48. clear_content()

#49. .preamble 实例属性

#50. .epilogue

#51. .defects.

#52 class email.message.MIMEPart( policy =default)

#53. 
