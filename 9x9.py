#!/usr/local/bin/python3
#打印九九乘法表
for x in range(1, 10):
   for y in range(1, x+ 1):
     print(str(x)+'x'+str(y)+'=',x*y, end= '\t')
   else:
     print()
