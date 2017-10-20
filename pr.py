import os
n,k = map(int, input().strip().split())
y=[]
while True:
    x = list(map(int, input().strip().split()))
    y.append(x)
    if(x[0]==0):
        break

print(x)
print(y)
