# coding=utf8
"""
我们知道默认的dict(字典)是无序的，但是在某些情形我们需要保持dict的有序性，这个时候可以使用OrderedDict，它是dict的
一个subclass(子类)，但是在dict的基础上保持了dict的有序型，下面我们来看一下使用方法。
"""

from collections import OrderedDict

# 无序的dict
d = {'banana' : 3, 'apple' : 4, 'pear' : 1, 'orange' : 2}

# 将d 按照key 来排序
print(OrderedDict(sorted(d.items(), key=lambda t: t[0])))

# 将d 按照value 来排序
print(OrderedDict(sorted(d.items(), key=lambda t: t[1])))

# 将d 按照key 的长度来排序
print(OrderedDict(sorted(d.items(), key=lambda t: len(t[0]))))


"""
使用popitem(last=True)方法可以让我们按照LIFO(先进后出)的顺序删除dict中的key-value，即删除最后一个插入的键值对，
如果last=False就按照FIFO(先进先出)删除dict中key-value。
"""

d = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print(d)
print(d.popitem())
print(d.popitem(last=False))


"""
使用move_to_end(key, last=True)来改变有序的OrderedDict对象的key-value顺序，通过这个方法我们可以将排序好的
OrderedDict对象中的任意一个key-value插入到字典的开头或者结尾。
"""
d = OrderedDict.fromkeys('abcde')
print(d)
# 将key为b的key-value对移动到dict的最后
d.move_to_end('b')
print(''.join(d.keys()))
# 将key为b的key-value对移动到dict的最前面
d.move_to_end('b', last=False)
print(''.join(d.keys()))

