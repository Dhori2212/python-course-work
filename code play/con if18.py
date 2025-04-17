while True:
    a=input("enter y for going  forword (enter n exit the loop :)")
    if (a!="n"):
        b=int(input("enter the number :"))
        if (b>0 and b%2==0):
            print(b,"is positive and even number ")
        elif(b>0 and b%2==1):
            print(b,"is positive and not a even number (odd number)")   
        else:
            print(b,"is negitive number")     
    else:
        break