l=list(map(int,input("Enter the list: ").split()))
maxl=l[0]
minl=l[0]
for i in range(l,len(l)):
    if l[i]>maxl:
        maxl=l[i]
    if l[i]<minl:
       minl=l[i]
print("maximun: ",maxl)
print("minimun: ",minl)
    