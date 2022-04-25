

needles = {'franck_gxu@outlook.com','franckisses@gmail.com'}
haystack = {'842549758@qq.com', '12345123@qq.com','franck_gxu@outlook.com','franckisses@gmail.com'}

found = len(set(needles) & set(haystack))

print(found)

found = len(set(needles).intersection(haystack))
print(found)
