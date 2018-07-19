## 1. 字符串
### 字符串分割
Python中使用split()函数进行字符串分割，分割后得到一个字符串列表。

例如按照逗号分割字符串：

    >>> s='abc,def,ghi'
    >>> strings=s.split(',')
    >>> print(strings)
    ['abc', 'def', 'ghi']

### 字符串合并
Python中使用join()函数进行字符串合并，与split()相反。

    >>> ':'.join(['abc', 'def', 'ghi'])
    'abc:def:ghi'

### 格式化字符串
使用%格式化字符串,可以使用格式化转换说明符控制输出字符串的精度。例如%.3f表示将输出字符串转换为保留小数点后3位的浮点数。

    >>> humidity,temperature=70,30
    >>> s="Today's temperature is %s degrees, and the humidity is %s%%."%(temperature,humidity)
    >>> print(s)
    Today's temperature is 30 degrees, and the humidity is 70%.
    >>> s="Today's temperature is %.1f degrees, and the humidity is %.1f%%."%(temperature,humidity)
    Today's temperature is 30.0 degrees, and the humidity is 70.0%.

在Python3.6以后的版本中可以使用F-string特征来格式化字符串，在字符串前加上一个字符f，在字符串中使用{}将表达式包起来便可以格式化字符串。shi用F-string格式化字符串速度最快。

    >>> s=f"Today's temperature is {temperature} degrees, and the humidity is {humidity}%."
    >>>print(s)
    Today's temperature is 30 degrees, and the humidity is 70%.

## 2. 文件
### 打开文件
使用open()函数可以在Python中打开磁盘上的文件，并返回一个文件对象。该文件对象是可以按行迭代的，也就是说在进行迭代操作时，该文件对象会返回一行字符串。

首先在目录下创建一个文本文件，命名为data.txt，在内部任意输入字符串。

随后在Python中运行下列代码：

    f=open('data.txt')
    for i in f:
        print(i)
    f.close()

代码便将文件一行行的输出到控制台中。在使用完文件对象后需要及时将文件对象关闭，避免造成文件读写冲突。使用f.close()便可关闭文件解除占用。

每次都要使用close()关闭文件显得很麻烦，因此可以使用with语句，将对文件的处理包含在with语句块中，当语句块运行完毕后自动释放文件对象。

    with open('data.txt') as f:
        for i in f:
            print(i)

### 写入文件
使用open()可以打开一个可供写入的文件，需要在open()函数中新增一个参数表示要对该文件进行何种操作。如果该文件不存在，代码将会在指定目录下创建一个文件供写入。使用write()函数写入文件。

    with open('data.txt','w') as f:
        f.write('hello')

## 3. 字典
字典是一种基于键值对（key-value）的数据类型。

### 字典的定义
直接使用{}定义字典，用:分割键和值，逗号分隔不同的键值对。
    
    myDict={'a':1234,'b':3456,'c':6789}

### 字典的访问
使用[key]访问字典内的value。

    >>> myDict['a']
    1234
    >>> myDict['b']
    3456

### 字典的赋值
和列表类似，只不过将列表的索引值换成key值。如果字典内本没有指定的key值，那么程序将会在字典中创建该键值对。

    >>> myDict['a']=431
    >>> myDict['a']
    431

### 字典的删除
使用pop()函数，pop()函数的参数为需要删除的键值对的键

    >>> myDict={'a':1234,'b':3456,'c':6789}
    >>> myDict.pop('c')
    6789
    >>> myDict
    {'a':1234,'b':3456}

### 字典的循环
字典是一个可迭代的对象，因此可以将其放在for循环中，每次迭代返回的为字典的键。

    >>> myDict={'a':1234,'b':3456,'c':6789}
    >>> for i in myDict:
            print(i,myDict[i])

    a 1234
    b 3456
    c 6789
    

## 练习题
### 统计下列字符串中除了空格外所有字符的数量。要求将字符与数量以key-value形式存储在一个字典中，如`{'a':3,'b':5  ……}`，并将其保存在文件中。

文件格式：

a,3

b,5

...


字符串：

    string = """Someone once said: "Don't be afraid if you find a crack on your soul, because that'll be where the sunshine comes in." There're too many wonderful things in this world. But life is so short and fragile. I want the authentic feeling that surpasses dreaming -- a love that is true and never fleeting. I want this for myself as well as for you. I'd like it for the world, if possible. Maybe God wants us to meet a few wrong people before meeting the right one, so that when it finally meet the person, it will know how to be grateful. 
    """

提示：
利用循环遍历字符串中每个字符，利用字典统计每个字符出现的次数。

### 答案

    string = """Someone once said: "Don't be afraid if you find a crack on your soul, because that'll be where the sunshine comes in." There're too many wonderful things in this world. But life is so short and fragile. I want the authentic feeling that surpasses dreaming -- a love that is true and never fleeting. I want this for myself as well as for you. I'd like it for the world, if possible. Maybe God wants us to meet a few wrong people before meeting the right one, so that when it finally meet the person, it will know how to be grateful. 
    """
    mydict={}

    for i in string:
        if i==" " or i=="\n":
            continue
        mydict[i]=string.count(i)

    print(mydict)
