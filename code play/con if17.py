while True:
    n=int(input("enter the number:"))
    is_prime=0
    for i in range(2,(n//2)+1):
        if(n%i==0):
            is_prime+=1
    if(is_prime==0):
        print(n,"prime number")
    else:
        print(n,"not a prime number")