n = int(input())
k = bin(n)[2:]
c = 1
d = []
for i in range(len(k)-1):
    if k[i]=='1' and k[i+1]=='1':
        c+=1
        d.append(c)
    else:
        d.append(c)
        c=1
print(max(d))
