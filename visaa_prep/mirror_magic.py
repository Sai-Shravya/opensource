def mirror_image(matrix):
    for i in range(len(matrix)):
        matrix[i]=matrix[i][::-1]
    return matrix
n=int(input())
matrix=[list(map(int,input().split()))for _ in range(n)]
m=mirror_image(matrix)
for row in m:
    print(" ".join(map(str, row)))
