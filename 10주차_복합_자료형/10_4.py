# 한 줄 입력을 공백 기준으로 나눠 리스트로 저장
items = input().split()

numbers = []  # 숫자만 저장
letters = []  # 문자만 저장

# 숫자와 문자를 분리
for x in items:
    if x.isdigit():          # 숫자라면
        numbers.append(int(x))  # 정렬 위해 정수로 변환
    else:                    # 문자라면
        letters.append(x)

# 각각 정렬
numbers.sort()
letters.sort()

# 출력: 숫자 먼저, 그다음 문자
for n in numbers:
    print(n, end=" ")

for ch in letters:
    print(ch, end=" ")