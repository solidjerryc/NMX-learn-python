## 2018/07/04 Python 练习题

### **随机生成含有100个整数的列表，计算这100个数字的平均值、样本方差以及中位数。**

提示：先利用循环随机生成一个含有100个整数的列表，再根据公式计算这些数据的平均值、样本方差以及中位数。

<img src="http://latex.codecogs.com/gif.latex?\overline{x}=\frac{{}\sum_{i=1}^{n}{x_i}}{n}" />
<img src="http://latex.codecogs.com/gif.latex?s^2=\frac{{}\sum_{i=1}^{n}{(x_i-\overline{x})^2}}{n-1}" />

当样本个数n为奇数时，中位数为数据中按升序排列的第<img src="http://latex.codecogs.com/gif.latex?\frac{n+1}{2}" />个样本，当n为偶数时，中位数为数据中按升序排列的第<img src="http://latex.codecogs.com/gif.latex?\frac{n}{2}" />个样本与第<img src="http://latex.codecogs.com/gif.latex?\frac{n}{2}+1" />个样本的均值。

Python生成随机数需要使用到random模块，方法如下：

    import random #导入模块

    # random.random函数能生成0-1之间的随机浮点数
    a=random.random() 

    # random.randint函数能生成制定区间内的随机整数
    b=random.randint(0,100) # 生成一个0-100之间的随机整数

    # random.gauss函数能生成正态分布的随机数
    c=random.gauss(0,1) # 生成一个服从均值为0，标准差为1的标准正态分布随机数
