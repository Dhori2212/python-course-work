while True:
    n=int(input("enter the number :"))
    if n!=0:
        if(n%3==0 and n%7==0):
            print(n," number is divisible  by 3 and 7")
        elif(n%3==0):
            print(n,"Number is divisible  by 3 only")
        elif(n%7==0):
            print(n,"Number is divisible  by 7 only")
        else:
            print(n," Number is not divisible")
    else:
        break