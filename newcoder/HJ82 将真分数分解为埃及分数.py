"""
描述
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
注：真分数指分子小于分母的分数，分子和分母有可能gcd不为1！
如有多个解，请输出任意一个。


输入描述：
输入一个真分数，String型

输出描述：
输出分解后的string

示例1
输入：
8/11
2/4
复制
输出：
1/2+1/5+1/55+1/110
1/3+1/6
复制
说明：
第二个样例直接输出1/2也是可以的    


#解题思路:将真分数(a/b)拆分成a*(1/b),也就是a个1/b,然后我们从大到小依次找出a中能被B整除的数.
比如: 5/8 这个真分数首先我们看,5不能被8整除,但是4可以,那从5中把4分离出来,变成1+4,剩余的1不能拆分,那埃及分数就是1/8+1/2

再比如:7/8这个真分数,首先我们看,7不能被8整除,6不能被8整除,5不能被8整除,4可以整除,分子分离出4,还剩3,我们看3不能整除,2能整除,分离出2,还剩1, 埃及分数:1/8+1/4+1/2
翻译成以下代码:
"""
import sys

for fs in sys.stdin.readlines():
    
    fzfm =fs.strip("\n").split("/")
    fz = int(fzfm[0])
    fm = int(fzfm[1])
    out_string = "" 
    num = fz
    zy = num
    contt = 0
    while True:
        try:
            if fm % zy == 0:
                if contt == 0:
                    out_string += ("1/" + str(fm // zy))
                else:
                    out_string += ("+1/" + str(fm // zy))
                    
                fz = fz - zy
                contt +=1
                zy = fz
                if fz == 0:
                    print(out_string)
                    break
                
            else:
                zy -= 1
                if zy == 0:
                    break
            
        except Exception:
            pass
    

