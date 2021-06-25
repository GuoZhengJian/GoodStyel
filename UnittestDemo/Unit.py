# -*- coding: utf-8 -*-

class Demo:
    """
    类或方法的第一行字符串为文档字符串。可以使用doctest模块来收集文档字符串， 在其中
    查找交互式会话，并以一系列测试的形式执行它们。
    
    要测试该单元, 通常会创建一个独立模块用于测试。如 TestUnit.py
    
    文档字符串通常会包含简短的交互例子:
    >>> Demo('Hello Word').back_str()
    'Hello Word'
    
    >>> Demo(5).back_nums()
    5
    
    >>> Demo(5).back_list()
    [0, 1, 2, 3, 4]
    
    >>> Demo(20).back_list()
    Traceback (innermost last):
        ...
    ValueError: number must be > 10

    """
    def __init__(self, number):
        self.number = number
        
    def back_str(self):
        return self.number
    
    def back_nums(self):
        return self.number
    
    def back_list(self):
        if self.number > 10:
            raise ValueError('number must be > 10')
        return [i for i in range(self.number)]
