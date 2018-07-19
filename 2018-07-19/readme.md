## 1. Python基础语句
### 链式赋值与增量赋值

Python中可以使用将一个值同时赋值给多个变量，这样的写法叫链式赋值。例如：

    x = y = z = 10

增量赋值是指给变量固定加上(加减乘除均可)某个固定值的复制方法。例如`x+=1`，等价于`x=x+1`。同样地，下列写法均可：

    x += 2
    y -= 1
    z *= 4
    w /= 5

### 与或非
在Python中与、或、非逻辑运算使用and、or、not表示。
#### 与（and）
当and运算符两边的表达式都为True时该式输出True，其中任意有一个为假时输出假。值得注意的是当Python计算 `A and B ` 时，如果表达式A的值为False，那么程序将不会计算表达式B直接输出False。

#### 或（or）
当or运算符两边的表达式有任意一个为True时该式输出True，两边都为假时输出假。

#### 非（not）
输出事件A的反面。

| a |  b|a and b|a or b|not a|
|--|--|--|--|--|
|Ture|True|True|True|False|
|False|True|False|True|True|
|True|False|False|True|False|
|False|False|False|False|True|

如果逻辑运算符前后没有接布尔表达式，而是跟了其他变量，那么and运算将会输出后面那个变量的值，or会输出前面那个变量的值。而对某变量执行not计算时，当该变量为0、''(空字符串)时，该表达式会输出True，反之输出False。

    >>> a=0
    >>> b=2
    >>> a and b
    2
    >>> a or b
    0
    >>> not a
    True
    >>> not b
    False

### 列表推导式
在某些特定的循环语句中，可以将这个语句简化为列表推导式————一种轻量化的循环。
例如下列语句，有一个列表a，现在需要将列表a中的每一个元素乘以3输出为一个列表，那么常规的写法如下：

    a=[1,2,3,4,5,6,7]
    b=[]
    for i in a:
        b.append(i*3)
    
使用列表推导式可以将上述代码简化为：

    b = [i*3 for i in a]

当对上述需要
