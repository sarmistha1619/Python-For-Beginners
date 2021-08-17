# series : 1*2*3*4...n

n=int(input("give the last value: "))

m=1
for i in range(1,n+1):
    m=m*i
    print(i, end=" ")
print(m)