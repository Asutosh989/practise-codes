z=int(input())
g=int(input())
x=1
c=1
for i in range(1,g):
    if(x>z):
        break
    else:
        x+=i
        c+=1
if z>x:
    a=z-x
    c+=(a//g)
    if(a%g!=0):
        c+=1
print(c)
