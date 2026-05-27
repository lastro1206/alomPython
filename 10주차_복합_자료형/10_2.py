n = int(input())

# 입력받은 n개의 정수를 리스트로 저장
arr = [int(input()) for _ in range(n)]

even = []
odd = []
diff = []

# 짝수/홀수를 분리
for i in range(n):
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

# 짝수: 중복 제거 후 오름차순, 홀수: 중복 제거 후 내림차순
even = sorted(list(set(even)))
odd = sorted(list(set(odd)), reverse=True)

# 두 리스트 중 짧은 길이까지만 뺄셈 연산
min_len = min(len(even), len(odd))
for i in range(min_len):
    diff.append(even[i] - odd[i])

# 홀수가 먼저 끝나면 남은 짝수는 그대로 추가
for i in range(min_len, len(even)):
    diff.append(even[i])

print("Even = ", even)
print("Odd = ", odd)
print("Difference = ", diff)