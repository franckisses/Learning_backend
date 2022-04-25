

needles = {'franck_gxu@outlook.com','franckisses@gmail.com'}
haystack = {'842549758@qq.com', '12345123@qq.com','franck_gxu@outlook.com','franckisses@gmail.com'}

found =0

for n in needles:
    if n in haystack:
        found += 1
 

print(found)
