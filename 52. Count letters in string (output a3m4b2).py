#input: aaaffv
#output : a3f2v1

s= "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
n= input("give a string line : ")

for i in s:
    c=n.count(i)
    if c>=1:
        print(i,end='')
        print(c,end='')
