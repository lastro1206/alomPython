n = int(input())

words = []
for _ in range(n):
    words.append(input().strip())

# 중복 제거 후, (길이, 단어) 기준으로 정렬
unique_words = sorted(list(set(words)), key=lambda w: (len(w), w))


for word in unique_words:
    print(word)