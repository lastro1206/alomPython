n = int(input())

total = 0

for i in range(0, n):
    num = int(input())
    if num == 0:
        break
    total += num

print("Total : %d" %total)