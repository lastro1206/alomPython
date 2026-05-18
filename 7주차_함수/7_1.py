def isOdd(num):
    cnt = 0
    if num % 2 == 0:
        return 0
    else:
        return 1

def countOdd(num):
    for i in range(1, num + 1):
        if isOdd(i):
            cnt += 1
    return cnt

num = int(input())
print(countOdd(num))