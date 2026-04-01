purchase = int(input())
membership = input()

discount = 0

if(membership == "VIP") :
    if(purchase >= 100000):
        discount = 20
    else :
        discount = 10
elif membership == "일반":
    if(purchase >= 50000):
        discount = 10
    else :
        discount = 5
elif membership == "비회원":
    discount = 0

print("할인율: %d%%" %discount)