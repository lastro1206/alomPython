n = int(input())
max_len = 0

for i in range(1, n + 1):
    string = input()
    if len(string) > max_len:
        max_len = len(string)
print(max_len)