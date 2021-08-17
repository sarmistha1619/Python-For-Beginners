# series: 1*2*3*4......n

n=int(input("n= "))
sum=1
for a in range(1,n+1):
    sum=sum*a
    print(a)
print(sum)