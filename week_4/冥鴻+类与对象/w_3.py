# 3：思考问题：
# #为什么会有对象方法 类方法 静态方法？我什么时候写什么类型的方法呢？
# #什么时候用？
# #写成不同的方法类型 有啥用呢？对我来说有啥用?
# #他们有什么区别呢？ #自己总结一波。


q=[12.213]
w=[12,12,34,'wqe']

# for i in range(1,5):  # 获取最大行
#
#     for j in range(1, 5):  # 获取最大列
#        c=i+j
#        q.append(c)
#     w.append(list(q))
#     q.clear()
# print(w)


q.append(list(w))
print(q)