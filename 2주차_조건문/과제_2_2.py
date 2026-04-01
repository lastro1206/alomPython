num = int(input()) 

one = num % 10
num //= 10 
ten = num % 10 
num //= 10 
hun = num
print("%d (%d+%d+%d)" %((one + ten + hun), hun, ten, one))