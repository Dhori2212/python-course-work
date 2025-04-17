while True:
    a=int(input("enter any number enter the prog (enter 0 exit the loop:)"))
    if(a!=0):
        b=input("enter the letter :")
        if(b==b.upper()):
            print(b," is upper letter")
        else:
            print(b," is lower letter") 
    else:
        break