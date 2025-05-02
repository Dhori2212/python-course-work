lst=list(map(int,input('Enter the list: ').split()))
sum=0
for i in lst:
    if i%5==0:
        sum+=i
print(f'sum of number dividible by 5: {sum}')