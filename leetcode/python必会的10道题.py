"""
1. 类继承

# 如何调用类A的show方法了。
"""


class A(object):
    def show(self):
        print("base show")


class B(A):
    def show(self):
        print("derived show")


obj = B()
obj.show()
obj.__class__ = A
obj.show()

"""
3. new 与 init
下面的代码输出是什么？
答案：
    # NEW 5
    # B INIT
    # B fn
    # NEW 20
    # INIT 20
    # A fn
解析：  
    使用new方法，可以决定返回那个对象，也就是创建对象之前，
    这个可以用于设计模式的单例、工厂模式。init是创建对象是调用的。
"""


class B(object):
    def fn(self):
        print('B fn')

    def __init__(self):
        print("B INIT")


class A(object):
    def fn(self):
        print('A fn')

    def __new__(cls, a):
        print("NEW", a)
        if a > 10:
            return super(A, cls).__new__(cls)
        return B()

    def __init__(self, a):
        print("INIT", a)


a1 = A(5)
a1.fn()
a2 = A(20)
a2.fn()


"""
4. Python list和dict生成

下面这段代码输出什么?

答案：
    # [3, 4]
    # [6, 8]
    # {2: 4, 4: 16, 6: 36}
    # {2: 'item4', 4: 'item16', 6: 'item36'}
    # {'h', 'd', 'r'}
"""
ls = [1, 2, 3, 4]
list1 = [i for i in ls if i > 2]
print(list1)

list2 = [i * 2 for i in ls if i > 2]
print(list2)

dic1 = {x: x ** 2 for x in (2, 4, 6)}
print(dic1)

dic2 = {x: 'item' + str(x ** 2) for x in (2, 4, 6)}
print(dic2)

set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)

"""
5. 全局和局部变量

下面这段代码输出什么?
答案：
    # 9
    # 9
解析：
    num不是个全局变量，所以每个函数都得到了自己的num拷贝，如果你想修改num，则必须用global关键字声明。
"""
num = 9
def f1():
    # global num
    num = 20

def f2():
    print(num)

f2()
f1()
f2()


"""
6. 交换两个变量的值
a = 8
b = 9
(a, b) = (b, a)
"""
a = 8
b = 9
(a, b) = (b, a)
print(a, b)


"""
7. 默认方法

如下的代码

class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print 'init'
    def mydefault(self):
        print 'default'

a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()
方法 fn1/fn2/fn3 都没有定义，添加代码，是没有定义的方法都调用mydefault函数，上面的代码应该输出

default
default
default
答案：

class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print 'init'
    def mydefault(self):
        print 'default'
    def __getattr__(self,name):
        return self.mydefault

a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()
方法getattr只有当没有定义的方法调用时，才是调用他。当fn1方法传入参数时，我们可以给mydefault方法增加一个*args不定参数来兼容。

class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print 'init'
    def mydefault(self,*args):
        print 'default:' + str(args[0])
    def __getattr__(self,name):
        print "other fn:",name
        return self.mydefault

a1 = A(10,20)
a1.fn1(33)
a1.fn2('hello')
a1.fn3(10)

"""


"""
9. 闭包

写一个函数，接收整数参数n，返回一个函数，
函数的功能是把函数的参数和n相乘并把结果返回。

答案:
"""
def mul(num):
    def gn(val):
        return val * num
    return gn
zw = mul(7)
print(zw(9))