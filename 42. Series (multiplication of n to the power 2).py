#series : 1*1*2*2*3*3*4*4*....n*n

n=int(input("value of n: "))

res=1
for i in range(1,n+1):
    res=res*i
    print(i, end=" ")
print(res)