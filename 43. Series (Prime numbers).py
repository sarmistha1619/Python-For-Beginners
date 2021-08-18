#series : prime numbers( 2,3,5,7,11....)

l=int(input("give the lower interval : "))
u=int(input("give the upper interval : "))
sum=0
for i in range(l,u+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
            sum=sum+i
print("sum", sum)