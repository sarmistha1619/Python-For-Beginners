#sum of even numbers: 2, 4, 6, ...n

a=int(input("give the value of last number"))
sum=0
for i in range(0,a+1,2):
    sum=sum+i
    print(i)
print("Sum is ", sum)