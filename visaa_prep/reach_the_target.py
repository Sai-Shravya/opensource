T=int(input())
for _ in range(T):
    X,Y=map(int, input().split())
    runs_required = (X-Y)+1
    print(runs_required)
