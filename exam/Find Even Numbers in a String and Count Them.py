string=input('Enter the numbers')
even=''
count=0
for i in string:
    if i.isdigit():
        if int(i)%2==0:
          even=even+' '+i
          count+=1
print(even)
print(count)

