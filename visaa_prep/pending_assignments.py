x,y,z=map(int,input().split())
m=z*60*24
n=x*y
if(n<=m):
    print("YES")
else:
    print("NO")
