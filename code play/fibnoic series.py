n=int(input("Enter the range: "))
a=0
b=1
print(a,b)
if n==0:
  print("None")
elif n==1:
    print(a)
elif n>=2:    
   print(a,b,sep=(" \n"))
   for i in range(n-2):
      c=a+b
      a=b
      b=c
      print(c)

