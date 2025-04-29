def num(c,d):
    c.append(d)
    print(d)

c=list(map(int,input("Enter the numbers:").split("  ")))
d=int(input("Enter the number:"))
num(c,d)