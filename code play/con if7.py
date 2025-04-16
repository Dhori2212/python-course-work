while True:
    n=int(input("enter the number :"))
    print("1.option str")
    print("2.option int")
    op=int(input("select the option :"))
    if(n!=0):
        if(op==1):
            if (len(str(n))==3):
                print("3-digit number")
            else:
                print("not a 3 digits number")
        elif(op==2):
            if(n>99 and n<1000):
                print("3 digit number")
            else:
                print("not a 3 digit number")
        else:
            print("select correct option ")
    else:
        break