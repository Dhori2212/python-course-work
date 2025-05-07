st=input("Enter a string: ")
vol='aeiouAEIOU'
res=''
for  i  in st:
    if i not in vol:
        res+=i
print('String without vowels:',res)
