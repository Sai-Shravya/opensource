def print_right_angle_triangle(n):
    
    num = 1
    for i in range(1,n+1):
       for j in range(i):
        print(num, end=" ")
        num += 1
       print()
n=int(input())
print_right_angle_triangle(n)
