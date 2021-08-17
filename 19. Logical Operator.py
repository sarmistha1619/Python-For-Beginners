# logical operator : or, and, not

a = 10
b = 20
c = 25

if a>b and a>c:
    print(f"{a} is greater.")
elif b>a and b>c:
    print(f"{b} is greater.")
else:
    print(f"{c} is greater.")