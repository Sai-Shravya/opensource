x=int(input())
coupon1 = x*0.1
coupon2 = 100
max_discount = max(coupon1, coupon2)
amount=x-max_discount
print(int(amount))
