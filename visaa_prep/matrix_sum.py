n=int(input())
matrix=[]
for _ in range(n):
    row =list(map(int, input().split()))
    matrix.append(row)
res=[]
for i in range(n):
    row_sum=sum(matrix[i])
    col_sum=sum(matrix[j][i] for j in range(n))
    res.append(row_sum+col_sum)
print(*res)
