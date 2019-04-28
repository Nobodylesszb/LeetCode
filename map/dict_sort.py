"""
按照key排序
"""
my_dict = {'lilee':25, 'age':24, 'phone':12}

print(sorted(my_dict.keys()))

"""
output:
['age', 'lilee', 'phone']
"""
"""
按照value值排序
"""
d = {'lilee':25, 'wangyan':21, 'liqun':32, 'age':19}
print(sorted(d.items(), key=lambda item:item[1]))
"""
output:
[('age', 19), ('wangyan', 21), ('lilee', 25), ('liqun', 32)]
"""

"""
使用operator的itemgetter进行排序
"""
import operator
r = sorted(d.items(), key=operator.itemgetter(1))
print(r)
"""
[('age', 19), ('wangyan', 21), ('lilee', 25), ('liqun', 32)]
"""