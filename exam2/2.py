n=int(input("Enter the number: "))
print(f'factors of {n}: ',end=' ')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')