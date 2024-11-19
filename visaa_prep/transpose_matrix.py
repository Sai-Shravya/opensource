n=int(input())
matrix=[]
for _ in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
t=[[matrix[j][i] for j in range(n)] for i in range(n)]
for row in t:
    print(*row)
