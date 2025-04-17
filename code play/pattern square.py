n=int(input("Enter the number: "))
for i in range(5):
    for j in range(5):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()