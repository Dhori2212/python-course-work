def  prime(num):
    for i in range(2,(n//2),+1):
        if num%i==0:
            return False
    return True

n=int(input("Enter the number:"))
if prime(n):
    print('prime number')
else:
    print('not ah prime')