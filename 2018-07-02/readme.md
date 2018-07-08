
# 1. Python基础知识
## 求余与整除
%表示求余

//表示整除

    >>>5%2
    1
    >>>5//2
    2


## 16进制、8进制与2进制
16进制用0x开头，8进制用 0o开头 二进制用0b开头

    >>>0x3f
    63
    >>>0o36
    30
    >>>0b010100110
    166

## 模块
用import关键字导入模块
用`from xxx import xxx`导入某个包中特定的函数

    import math
    from math import sin
    from math import *
    from math import floor,ceil

## 四舍五入、取整
round()四舍五入

math.ceil()向上取整

math.floor()向下取整

    >>>round(1.5)
    2
    >>>import math
    >>>math.floor(1.5)
    1
    >>>math.ceil(1.5)
    2

>ceil  v.在…装天花板

## 转义字符
    \n 换行
    \t 制表符
    \b 退格
    \' '
    \" "
    \\ \

    >>>print("abc\nabc")
    abc
    abc
    >>>print("abc\tabc")
    abc     abc
    >>>print("abc\babc")
    ababc
    >>>print('abc\'abc')
    abc'abc
    >>>print("abc\"abc")
    abc"abc
    >>>print("abc\\abc")
    abc\abc

## 原始字符串
在字符串前面加一个字母r，使得后面的字符串中所有字符原样输出，不被转义
    
    >>>print(r"abc\\abc")
    abc\\abc



# 2. 列表
## 索引
从0开始，负数代表倒数。

    >>>a=[1,2,3,4,5,6,7]
    >>>a[0]
    1
    >>>a[-2]
    6

## 分片
从列表中截取一段
参考书本

## 成员资格
in关键字

    if 'e' in 'hello':
        print("yes")

## 字符串是个特殊的列表

## 列表操作
* 赋值
* 删除 （注意尽量使用 `del()`）
* 分片赋值

## 列表方法
参照书2.3.3

数据结构相关知识：
* 栈：先进后出
* 队列：先进先出

## 元组
元组就是在Python中的一种不可变的序列，通常用来作为函数的返回值。比较简单。
在关系型数据库中，元组表示二维表的某行，例如下表：

|学号|姓名|课程|成绩|
|--|--|--|--|
|001|cbq|Python|100|
|002|nmx|Python|101|
||||

其中`(001,cbq,Python,100)`就是一个元组。

可以使用`list()`与`tuple()`将列表与元组互相转换。

# 3. 循环语句
## `while`循环
结构：

    while 条件:
        循环体

## `for`循环
for循环依赖于一个可迭代的对象，例如列表、元组、字符串、文件对象等等。相比于while循环，for循环一般不会出现死循环。

结构：

    for 变量 in 序列:
        循环体
