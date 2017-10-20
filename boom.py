s=input()
x,y=0,0
for w in s.split():
	x,y={"boom":(min(x+1,30),y),"ts":(max(x-1,0),y),"ding":(x,max(y-1,0)),"bing":(x,min(y+1,10))}[w]
print("%d %d"%(x,y))