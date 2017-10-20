n=int(input())
s=input()
d=list(s)
g = [s[i:j] for i in range(d) for j in range(i+1,d+1)]
print(g)
g.sort()
print(g)
print(g[len(g)-1])
if(len(list(set(d)))==len(d)):
    print(g[len(g)-1])
