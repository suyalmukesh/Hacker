import sys
import os
n = int(input())
stack = []
Max = []
for i in range(n):
    query = input()
    if query[0] == '1':
        query1, query2 = query.split(' ')
        stack.append(int(query2))
    elif query[0] == '2':
        stack.pop()
    elif query[0] == '3':
       a = max(stack)
       Max.append(a)

print(Max)


