sen=input("Enter  sentence: ")
word=input("Enter word to find: ")
if word in sen:
    print(f"The word '{word}' is found in the sentence. ")
else:
    print(f"The '{word}' is not found in the sentence. ")
