n=int(input())
attendance=list(map(int,input().split()))
a=0
p=0
for day in attendance:
    if day==0:
        p+=1
        a=max(a,p)
    else:
        p=0
print(a)
