while True:
   n=input("enter the latters :").lower()
   if n!="done":
       print("1.option")
       print("2.option")
       op=int(input("select option:"))
    
       if (op==1):
           vowel="a,e,i,o,u,A,E,I,O,U"
           if (n in vowel):
             print(n,"is vowel")
           else:
              print("not a vowel")
       elif(op==2):
          if(n=="a"or n=="e"or n=="i" or n=="o" or n=="u"):
             print(n,"vowle")
          else:
             print(n,"not a vowle")
   else:
      break