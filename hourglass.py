d=[]
q = []
for i in range(6):
    l=list(map(int,input().split()))
    d.append(l)
for i in range(1,5):
    for k in range(1,5):
        m = d[i][k]+d[i-1][k-1]+d[i-1][k]+d[i-1][k+1]+d[i+1][k-1]+d[i+1][k]+d[i+1][k+1]
        q.append(m)
print(max(q))
