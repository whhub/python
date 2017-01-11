# coding=utf8
"""
defaultdict(default_factory)在普通的dict(字典)之上添加了default_factory，使得key(键)不存在时会自动生成相应类型
的value(值)，default_factory参数可以指定成list, set, int等各种合法类型。
"""


from collections import defaultdict

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]

d = defaultdict(set)

for k, v in s:
    d[k].add(v)

print(d)
