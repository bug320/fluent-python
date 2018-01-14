# -*- coding: utf-8 -*-
"""
@author  : bug320
@purpose : learn&try Ch5: 一等函数
@date    : 2018-01-03
@note    : `learn&try` `流畅的python`
"""

"""1. 函数基础"""

"""eg 1.1 基础定义使用的函数"""
def funN(n):
    """ return n! """
    return 1 if n < 2 else n * funN(n-1)
    pass

print funN(10)     # 3628800
print funN.__doc__ # return n!
print type(funN)   # <type 'function'>

"""
__doc__ : function 类的一个属性，用来生成一个对象的注释文本。在 python 交互控制太中，使用
help(funN) 和 `print funN.__doc__` 输出一样。
funN    : 函数对象的名字，是 function 类的一个实例。
"""

# """eg 1.2 通过不同的名称调用函数，并把函数作为参数进行传递。"""

fact = funN
print fact
fact(10)
print map(fact, range(11)
