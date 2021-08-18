import random_number

for i in range(1,6):
    n = int(input("give a number between 1 to 10 :"))
    ran = random_number.random_number(1, 11)

    if n == ran:
        print("won")
    else:
        print("lost")
        print(r)
