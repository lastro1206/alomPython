p1 = input()
p2 = input()

left = 0
right = 0

if(p1 == p2):
    left = 5
    right = 5
elif(p1 == 'N' and p1 != p2) :
    left = 10
    right = 5
elif(p2 == 'N' and p1 != p2) :
    left = 0
    right = 10
else :
    left = 0
    right = 0

print("Left:", left)
print("Right:", right)