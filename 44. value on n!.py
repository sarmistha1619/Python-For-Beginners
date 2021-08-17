#n!=1*2*3*(n-1)
#n= 4
n= int(input("give n: "))
fac=1
for i in range(1,n):
    fac=fac*i
    print(i)

print("factorial", fac)
