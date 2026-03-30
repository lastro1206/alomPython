sum = 0
count = 0
while True:
    num = int(input())
    sum += num
    count += 1
    if sum >= 20 or num == 4:
        break
print("Total = %d" %sum)
print("Count = %d" %count)