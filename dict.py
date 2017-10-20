n = int(input())
d={}
for i in range(n):
    k,v = input().split()
    d[k] = v
while True:
    l = input()
    if (l!=''):
        try:
            print(l+"="+d[l])
        except:
            print('Not found')
    else:
        break
