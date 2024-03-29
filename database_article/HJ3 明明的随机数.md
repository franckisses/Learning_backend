OD

### HJ3: 明明的随机数

## 描述

明明生成了*N*个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。

数据范围： 1≤*n*≤1000 ，输入的数字大小满足 1≤*v**a**l*≤500 

### 输入描述：

第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表明明生成的随机数。 具体格式可以参考下面的"示例"。

### 输出描述：

输出多行，表示输入数据处理后的结果

## 示例1

```

输入：
3
2
2
1
输出
1
2
输入解释：
第一个数字是3，也即这个小样例的N=3，说明用计算机生成了3个1到500之间的随机整数，接下来每行一个随机数字，共3行，也即这3个随机数字为：
2
2
1
所以样例的输出为：
1
2       
```

code

```python
n = input()
my_list = []
for i in range(int(n)):
    my_list.append(int(input()))
for j in sorted(set(my_list)):
    print(j)
```

### HJ3 质数因子

## 描述

功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）

数据范围： 1≤*n*≤2×10^9+14 

### 输入描述：

输入一个整数

### 输出描述：

按照从小到大的顺序输出它的所有质数的因子，以空格隔开。

## 示例1

```
输入
180
输出
2 2 3 3 5

```

code:

```

import math 

num = int(input())
s = ''
prime = 2
while prime < math.sqrt(num)+1:
    if num % prime != 0:
        prime += 1
    else:
        num = num // prime
        s += str(prime) + ' '
        prime = 2
if num >=2:
    s += str(num) + ' '

print(s) 
```



### HJ16

王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：

| 主件   | 附件           |
| ------ | -------------- |
| 电脑   | 打印机，扫描仪 |
| 书柜   | 图书           |
| 书桌   | 台灯，文具     |
| 工作椅 | 无             |

如果要买归类为附件的物品，必须先买该附件所属的主件，且每件物品只能购买一次。

每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。

王强查到了每件物品的价格（都是 10 元的整数倍），而他只有 N 元的预算。除此之外，他给每件物品规定了一个重要度，用整数 1 **~** 5 表示。他希望在花费不超过 N 元的前提下，使自己的满意度达到最大。

### 输入描述：

输入的第 1 行，为两个正整数N，m，用一个空格隔开：

（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。

从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q

（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 **~** 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）

### 输出描述：

 输出一个正整数，为张强可以获得的最大的满意度。

## 示例1

输入：

```
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
```

输出：

```
2200
```

## 示例2

输入：

```
50 5
20 3 5
20 3 5
10 3 0
10 2 0
10 1 0
```

输出：

```
130
```

说明：

```
由第1行可知总钱数N为50以及希望购买的物品个数m为5；
第2和第3行的q为5，说明它们都是编号为5的物品的附件；
第4~6行的q都为0，说明它们都是主件，它们的编号依次为3~5；
所以物品的价格与重要度乘积的总和的最大值为10*1+20*3+20*3=130 
```

code:

```
n, m = map(int,input().split())
primary, annex = {}, {}
for i in range(1,m+1):
    x, y, z = map(int, input().split())
    if z==0:
        primary[i] = [x, y]
    else:
        if z in annex:
            annex[z].append([x, y])
        else:
            annex[z] = [[x,y]]
dp = [0]*(n+1)
for key in primary:
    w, v= [], []
    w.append(primary[key][0])#1、主件
    v.append(primary[key][0]*primary[key][1])
    if key in annex:#存在附件
        w.append(w[0]+annex[key][0][0])#2、主件+附件1
        v.append(v[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:#附件个数为2
            w.append(w[0]+annex[key][1][0])#3、主件+附件2
            v.append(v[0]+annex[key][1][0]*annex[key][1][1])
            w.append(w[0]+annex[key][0][0]+annex[key][1][0])#4、主件+附件1+附件2
            v.append(v[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    for j in range(n,-1,-10):#物品的价格是10的整数倍
        for k in range(len(w)):
            if j-w[k]>=0:
                dp[j] = max(dp[j], dp[j-w[k]]+v[k])   
print(dp[n])

```

# HJ 17坐标移动

开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10; A1A; $%$; YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

\+  A10  = （-10,0）

\+  S20  = (-10,-20)

\+  W10 = (-10,-10)

\+  D30 = (20,-10)

\+  x  = 无效

\+  A1A  = 无效

\+  B10A11  = 无效

\+ 一个空 不影响

\+  A10 = (10,-10)

结果 （10， -10）

数据范围：每组输入的字符串长度满足 1≤�≤10000 1≤*n*≤10000 ，坐标保证满足 −231≤�,�≤231−1 −231≤*x*,*y*≤231−1 ，且数字部分仅含正数

### 输入描述：

一行字符串

### 输出描述：

最终坐标，以逗号分隔

## 示例1

输入：

```
A10;S20;W10;D30;X;A1A;B10A11;;A10;
```

输出：

```
10,-10
```

## 示例2

输入：

```
ABC;AKL;DA1;
```

输出：

```
0,0
```

code

```o
BEGIN = [0, 0]
all_step = input().split(';')

def move(direction, step, BEGIN):
    if direction == 'A':
        BEGIN[0] = BEGIN[0]-step
    elif direction == 'D':
        BEGIN[0] = BEGIN[0] + step
    elif direction == 'W':
        BEGIN[1] = BEGIN[1] + step
    elif direction == 'S':
        BEGIN[1] = BEGIN[1] - step 

for i in all_step:
    if i[:1] in ('A','D','W', 'S') and i[1:].isdigit():
        move(i[:1], int(i[1:]), BEGIN)

print(BEGIN[0],',',BEGIN[1],sep='')
```



