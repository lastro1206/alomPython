n = int(input())

arr = [[0] * n for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(n):
        cnt += 1
        arr[i][j] = cnt

for i in range(n):
    for j in range(n):
        print(arr[j][i], end=" ")
    print()