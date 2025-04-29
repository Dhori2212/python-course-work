n=int(input("Enter the range: "))
temp=n
rev=0
while n>0:
    rev=rev*10+(n%10)
    n=n//10
    print(rev)
if rev==temp:
    print("pd")
else:
    print("npd")