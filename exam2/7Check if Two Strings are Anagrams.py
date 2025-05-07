st1=input("String 1: ")
st2=input("String 2: ")
if len(st1)==len(st2):
   for i in st1:
    if i not in st2:
        print("The strings are not anagrams.")
        break
    else:
        print("The stringsd are anagrams.")