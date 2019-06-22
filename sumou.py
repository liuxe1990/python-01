#!/usr/local/bin/python3
sum = 0
i = 0
while i <= 100:
  i+= 1
  if i % 2:
    continue
  sum += i
print('result is %d'%sum)
