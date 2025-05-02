lst=list(map(int,input("Enter list elements: ").split()))
tar=int(input("Target sum: "))
res=[]
while lst:
    f=lst[0]
    s=tar-lst[0]
    lst.remove(f)
    if s in lst:
        res.append((f,s))
        lst.remove(s)
print(f"pairs with sum {tar}: {res}")