n=int(input("Enter the number: "))
for i in range(1,n+1):
    if i<=((n+1)//2):
        print("* "*i)
     else:
        print("* ",*(n-i+1))
    