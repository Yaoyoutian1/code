""" python 基础

    包括一些基本操作和注意事项


    序列化,   可变对象,不可变对象
"""

'''
切片 对于序列的操作
[开始位置索引,结束索引+1,步长]  索引可以为负数
[:] 复制


函数默认值只会初始化一次
可选参数,关键字参数,形式参数

'''
oldage=20
# 默认值只初始化一次
def as_ok(name:str, age=oldage, sex="男", remarks="这个男孩来自中国")->str:
    """
    函数注解
    
    """
    i = 1
    while True:
        ok = input(name)
        if ok in ('yyt', 'y', 'yy'):
            print("我叫姚友田是个{0},今年{1}岁,{2}".format(age, sex, remarks))
        elif ok in ("no"):
            print(remarks)
        else:
            print("hello")

oldage=22
as_ok('y')