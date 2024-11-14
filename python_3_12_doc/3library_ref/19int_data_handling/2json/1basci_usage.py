#1. json.dump( obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, ...)  返回一个fp 支持 .write()的file-like object
#2. json.dumps(...)对比1，返回str，

#3. json.load( fp, ...)  返回一个python对象，其中fp肯定是支持  .read()操作了
#4. json.loads(...) 将一个str(包含json文档的str， 反序列化为一个python对象
