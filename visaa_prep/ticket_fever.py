t=int(input())
result=[]
for _ in range(t):
    n,m = map(int, input().split())
    result.append(max(0, n-m))
for res in result:
    print(res)
