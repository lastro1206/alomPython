n = int(input())

num = [int(input()) for _ in range(n)]

avg = sum(num) / n
mid = n // 2

print("Avg = %.2f" %avg)
print("Mid = %d" %num[mid])