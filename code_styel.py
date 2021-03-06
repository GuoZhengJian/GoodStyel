"""
避免使用(.)运算符 (使用from math import sqrt和sqtr(x) 比 import math和math.sqrt(x) 要快)
不过不应该在所有位置都消除属性查找, 因为这会使代码非常难以理解。但对于注重性能的部分，这是一种有用的技术；
如下述： 
    from doctest import testmod和testmod() 性能更好, 但是在代码很多的情况下不容易理解, 且涉及命名空间问题， 
    import doctest和doctest.testmod() 更容易理解, 但是在涉及大量调用属性的情况下会很慢。
"""
from doctest import testmod

    
class CodeStyel:
    """
    这是一个良好的文档格式示例类, 它包含了文档格式和文档测试。
    该类定义了以下属性:
        numx: None; 分子 
        numy: None; 分子
        numz: None; 分母
        
    示例:
    >>> CodeStyel(numx=3, numy=2).func1(2)
    [0, 1, 2]
    
    # 文档内也可以注释, 参考本条设置
    # >>> CodeStyel(numx=6, numy=3).func1(2)
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    """

    # __slots__ = ('x', 'y')
    
    def __init__(self, numx=None, numy=None, numz=None, state=True):
        """
        如果该类有很多实例, 那么可以使用__slots__限制属性名称设置, 这样可以有效减少内存和执行时间
        
        有起名困难症的同学可以使用"__私有属性", 这样在子类继承的时候就不需要考虑命名冲突, 
        (注意:使用私有属性后就无法使用__slots__限制属性名称)
        """
        self.__x = numx
        self.__y = numy
        # self.__z = numz    # AttributeError: 'DocStyel' object has no attribute 'z'
        
    @装饰器函数
    def func1(self, num):
        """
        多用装饰器来处理对象的参数, 把参数处理和目标函数功能分开写, 便于维护
        
        使用内置类型来操作和存储数据 (元组,列表,集合,字典完全是由C实现的, 且是最优的数据结构)
        内置函数有的功能, 不要造轮子。
        不要添加层 (尽量使用文档介绍的方法使用对象或函数, 如{A:20} 要比 dict(A=20)快很多)
        尽量用try来引发异常 (在能使用try...except...raise...的情况下, 不要使用if...raise...)
        尽量使用函数编程和迭代 (列表包含, 生成器表达式, 生成器, 协程和闭包是很高效的处理方式, 尤其是对数据处理而言)
        """
        try:
            return [i for i in range(int(self.__x * self.__y / num))]
        except TypeError:
            raise TypeError('类型错误')
        
    #
    @property
    @staticmethod
    @classmethod
    def addfunction(cls):
        """
        多使用装饰器和元类
            节约内存和运行时间 - 因为这两种方法都是在调用时才会被实例化, 在不调用时不会占用额外的内存空间
            通过判断来确定不同的功能 - 对不常用的功能用判断状态来决定是否开启
        """
        pass
        
        
if __name__ == '__main__':
    testmod()