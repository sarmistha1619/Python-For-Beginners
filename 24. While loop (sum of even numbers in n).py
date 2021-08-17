n = int(input("give a number"))

i=1
sum=0
while i<n+1:
    if i%2==0:
        sum=sum+i
    i = i + 1

print(sum)