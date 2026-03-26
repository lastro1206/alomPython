km = int(input())
min = int(input())

hour = min / 60

km_per_hour = km / hour
print("Speed : %.3f km/h" %km_per_hour)
if(km_per_hour >= 80) :
    print("Fast")
elif(km_per_hour <= 30):
    print("Slow")
else :
    print("Normal")