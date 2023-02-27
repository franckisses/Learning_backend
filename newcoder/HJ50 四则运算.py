"""
描述
输入一个表达式（用字符串表示），求这个表达式的值。
保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。

数据范围：表达式计算结果和过程中满足 1∣val∣≤1000  ，字符串长度满足 1≤n≤1000 

输入描述：
输入一个算术表达式

输出描述：
得到计算结果

示例1
输入：
3+2*{1+2*[-4/(8-6)+7]}
复制
输出：
25
"""

# 将输入的表达式中的数字和符号区分开，并保存到列表中
def group(s):
    num, res = '', []
    for i, c in enumerate(s):
        if c.isdigit():
            num += c # 数字可能有很多位数
        else:
            if num:
                res.append(num)
                num = ''
            if c == '-': # 负数的判断
                if (i == 0) or (s[i-1] in '+-*/([{'):
                    num += c
                    continue
            res.append(c)
    if num:
        res.append(num)
    return res

while True:
    try:
        s = input()
        lst = group(s)
        stack_n, stack_op = [], []
        '''
            遍历数字和符号列表lst：
            1.如果遇到数字，添加到数字栈stack_n中；
            2.如果遇到*/([{这些符号，直接添加到符号栈stack_op中；
            3.如果遇到+-号:
                (1).如果符号栈stack_op为空或栈顶元素是左括号([{的话，直接入栈；
                (2).如果符号栈stack_op不为空，则不断从符号栈stack_op中弹出一个符号，
                    同时从数字栈stack_n中弹出两个数字进行运算，并将运算结果保存到数字栈stack_n中。
                    期间若遇到左括号([{，则跳出循环，最后再将加号+或者减号-添加到符号栈中。
            4.如果遇到右括号)]}，在栈顶元素不是左括号([{之前，不断地取出数字和符号进行运算，
              同时将结果保存到数字栈stack_n中，最后删除左括号。
        '''
        for i in lst:
            if i not in '+-*/()[]{}': # 数字
                stack_n.append(i)
            elif i in '*/([{':
                stack_op.append(i)
            elif i in '+-':
                if len(stack_op) == 0 or stack_op[-1] in '([{':
                    stack_op.append(i)
                else:
                    while stack_op:
                        if stack_op[-1] in '([{':
                            break
                        op = stack_op.pop()
                        n2, n1 = stack_n.pop(), stack_n.pop()
                        stack_n.append(str(eval(n1 + op + n2)))
                    stack_op.append(i)
            elif i in ')]}':
                while stack_op[-1] not in '([{':
                    op = stack_op.pop()
                    n2, n1 = stack_n.pop(), stack_n.pop()
                    stack_n.append(str(int(eval(n1 + op + n2))))
                stack_op.pop()
        # 对数字栈和符号栈中剩余元素进行运算
        while stack_op:
            op = stack_op.pop()
            n2, n1 = stack_n.pop(), stack_n.pop()
            stack_n.append(str(int(eval(n1 + op + n2))))
        # 弹出并打印数字栈中最后一个数字，即运算结果
        print(stack_n.pop())
    except:
        break
