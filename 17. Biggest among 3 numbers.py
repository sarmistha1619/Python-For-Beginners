a = int(input("1st number: "))
b = int(input("2nd number: "))
c = int(input("3rd number: "))

if a>b:
    if a>c:
        print(f"{a} is the greatest")
    else:
        print(f"{c} is the greatest")
else:
    if b>c:
        print(f"{b} is the greatest")
    else:
        print(f"{c} is the greatest")