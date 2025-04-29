n=tuple(map(int,input('enter the numbers')))
sum=0
for i in (n):
    if i%2!=0:
        sum=sum+i
print(sum)