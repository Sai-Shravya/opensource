def unique_elements(arr):
    unique=[]
    for num in arr:
        if num not in unique:
            unique.append(num)
    return unique
n=int(input())
arr=list(map(int,input().split()))
print(" ".join(map(str,unique_elements(arr))))
