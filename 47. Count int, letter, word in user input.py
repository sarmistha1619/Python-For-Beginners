i=0
let=0
w=0

a=input("give an input: ")

for b in a:
    if '0'<=b<='9':
        i=i+1
    elif 'a'<=b<='z':
        let=let+1
    elif 'A'<=b<='Z':
        let=let+1
    elif b==' ':
        w=w+1

print("numbers: ", i)
print("letters : ",let)
print("words : ", w+1)