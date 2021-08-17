#sum of : 1, 2, 3, ..... n

n=int(input("give the value of n: "))

sum=0
for i in range(1, n+1):
    sum=sum+i
    print(i)
print(sum)