# stars

n=int(input("give value: "))

for i in range(1,n+1):
    print(i*"*")

for i in range(1,n+1):
    print((3*i-1)*"*")

for i in range(1,n+1):
    print((n-i)*"*")

for i in range(1,n+1):
    print((n-i)*" ", end=" ")
    print(i*"*")
