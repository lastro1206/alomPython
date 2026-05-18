import math

def lcm(n1, n2):
    return n1 * n2 // math.gcd(n1, n2)

n1 = int(input())
n2 = int(input())
print(lcm(n1, n2))