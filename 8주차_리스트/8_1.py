n = int(input())
arr = []

# 이 반복문에서는 반복되는 변수 (ex: i)가 필요하지 않으므로 _로 대신할 수 있음.
for _ in range(n):
    arr.append(int(input()))

# set(arr) == 중복 제거, 만약 길이가 1이면 모든 값이 동일하다는거.
if len(set(arr)) == 1:
    print("All values are identical.")
else:
    print("Max = %d" % max(arr))
    print("Min = %d" % min(arr))