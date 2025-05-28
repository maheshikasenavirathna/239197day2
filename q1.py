total=0
for i in range(1,11,1):
    sqr=i*i
    if ((sqr%4==0)):
        total+=sqr    
print("sum of squre numbers of numbers 1 to 1100 is:",total)