s=str(input())
vowels="aeiouAEIOU"
vow_count=0
const_count=0
for char in s:
    if char.isalpha():
        if char in vowels:
            vow_count+=1
        else:
            const_count+=1
print(f"{vow_count},{const_count}")
