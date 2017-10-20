m,i,k=map(int,input().split())
b=list(map(int,input().split()))
x=b.count(1)
diff=x-i
if(diff>=0):
    p,t,c,cost,initial=0,0,0,0,0
    while(p!=diff):
        if(b[t]==1):
            p+=1
        t+=1
    for j in range(t,m):
        if(b[j]==1):
            if c==0:
                cost=cost+j-initial
            else:
                cost=cost+((j-initial)*(c*k))
            c+=1
            i-=1
            initial=j
            if i==0:
                break
    print(cost)
else:
    print(-1)
