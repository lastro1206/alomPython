sum = 0
cnt = 0

while True:
    num = int(input())
    if num == 4:
        continue
    sum += num
    cnt += 1
    if sum >= 20:
        break
print("Total = %d" %sum)
print("Count = %d" %cnt)