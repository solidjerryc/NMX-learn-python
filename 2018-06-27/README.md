# 今日要点
## 1. Python入门
* 编译型语言和脚本型语言
* Python的运行方式（交互式和脚本式）
* 在哪写Python

## 2. Python的运行环境
* Mac OS自带的Python
* Anaconda集成运行环境

## 3. Python基础语法
* print() 输出函数
* input() 输入函数
* Python的变量类型（int，float，string）
* 赋值运算符（=）
* 算数运算符（+ - * / % **）
* 比较运算符（> < >= <= == !=）
* 条件语句（if elif else）
* Python是靠4个空格来区分语句块
* int() float() 强制转换函数 （字符串->数字）
* str() 字符串强制转换函数 （数字->字符串）
* 字符串相加

## 4. 今日例题
* 输入a,b两个数字，输出a+b的数值
* 输入a,b两个数字，若a>b，输出a+b的数值；若a<b，输出a-b的数值
* 求出任意一元二次方程的实数解
* 求出任意一元二次方程的复数解

## 5. 今日练习
输入任意三条边的数值，求出该三角形的面积。

（提示：首先需要判断该三条边是否能构成三角形，利用海伦公式求三角形的面积）

海伦公式（a,b,c为三边边长）：

<img src="http://latex.codecogs.com/gif.latex?p=\frac{a+b+c}2" />

$$p=\frac{a+b+c}2$$
$$S=\sqrt{p(p-a)(p-b)(p-c)}$$

测试数据：

1,2,3

3,4,5

2,3,3

3,6,1

7,7,6

10,10,10


    if a>1 and a<10:
        print("yes")
    elif a<1 and a>10:
        print("no")

    
