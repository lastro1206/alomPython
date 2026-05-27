n = int(input())

arr = []
one = n % 10
n //= 10
ten = n % 10
n //= 10
hun = n

arr.append(one ** 2)
arr.append(ten ** 2)
arr.append(hun ** 2)

print(sum(arr))