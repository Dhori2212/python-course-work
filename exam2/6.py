st=input("Enter a string: ")
s=set()
for i  in st:
    if i in s:
        print("First repeated character:",i)
        break
    else:
        s.add(i)
            