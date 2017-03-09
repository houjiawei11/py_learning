#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 字符串和编码
last=72 
new=85
r=(new-last)*100/last
print('rising %.1f %%' % r)

#使用list和tuple
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

#数字的输入 条件语句
# a = input('height: ')
# height = float(a)
# b = input('weight: ')
# weight = float(b)
height=1.7
weight=80
bmi=weight/(height*height)
if bmi<18.5:
	print('过轻')
elif bmi>=18.5 and bmi<25:
	print('正常')
else:
	print('过重')

#循环语句 for/while
sum=0
for x in list(range(101)):
	sum=sum+x
print('sum= %d' % sum)
sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print('sum= %d' % sum)

#输出十六进制数
n1 = hex(255)
print('n1=%s' % n1)