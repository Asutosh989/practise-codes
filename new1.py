n,r=int(input()),int(input())
z=1
x=''
if ((n>=2) and (r>=2)):
    for i in range(r-2):
        x+=str(i+2)
        z+=1
    print('1'+('0'*(n-z))+x)
elif(n==2 and r==1):
    print('1'*n)
else:
    print(0)
y=''
c=1
for i in range(r):
    y+=str(9-i)
print(('9'*(n-r))+y)
