#series : 1,3,5,7,....n

b=int(input("give the last value : "))
sum=0
for i in range(1,b+1,2):
    sum=sum+i
    print(i, end=" ")
print("sum is = ", sum)