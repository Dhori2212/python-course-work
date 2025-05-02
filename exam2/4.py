lst=list(map(int,input('Enter the list: ').split()))
avg=sum(lst)/len(lst)
print(f'Average: {avg}')
print('Number is greater than average: ',end=' ')
for i in lst:
    if i>avg:
        print(i,end=' ')