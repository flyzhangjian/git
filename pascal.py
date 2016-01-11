# !usr/bin/env python3
# _*_ coding:utf-8 _*_

import sys
def pascal(n):
	b=[1]
	a=0
	while a<n:
		yield b
		b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)] + [1]
		a=a+1

n=int(input())
for x in pascal(n):
	i,m=0,0
	while m<n-1:
		sys.stdout.write(' ')
		m=m+1
	print(x)
	n=n-1
