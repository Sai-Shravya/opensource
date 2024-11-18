n=int(input())
for i in range(1, n+1):
    left_triangle=''.join(map(str, range(1, i+1)))
    right_triangle=''.join(map(str,range(i,0,-1)))
    space=' '*(2*(n-i))
    print(f"{left_triangle}{space}{right_triangle}")
