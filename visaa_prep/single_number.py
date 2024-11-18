def single_number(arr):
    res=0
    for current_num in arr:
        res ^= current_num
    return res
n=int(input())
arr=list(map(int,input().split()))
print(single_number(arr))
