num = int(input())
cnt = 0
while num > 0:
    digit = num % 10
    cnt += 1
    num //= 10
print(cnt)