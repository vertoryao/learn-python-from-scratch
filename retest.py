import re
#.的使用
a = 'xy123'
b = re.findall('x.', a)
print(b)
