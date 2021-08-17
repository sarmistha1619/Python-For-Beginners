#series: 1 + 1/2 + 1/3 +.....1/n

n=int(input("enter the value of n: "))

sum=0
for i in range(1,n+1):
    sum=sum+1/i
    print(i)
print("result: ",sum)