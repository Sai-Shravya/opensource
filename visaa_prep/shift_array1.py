n=int(input())
arr=list(map(int,input().split()))
rot_arr=arr[1:]+arr[:1]
print(" ".join(map(str, rot_arr)))
