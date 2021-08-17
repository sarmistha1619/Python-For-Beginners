#series: n to the power 2 ( square of n)
# 1*1, 2*2, 3*3, .... n*n

n=int(input("give the value of n : "))
sum=0
for i in range(1,n+1):
    sum=sum+i*i
    print(i)
print("sum",sum)