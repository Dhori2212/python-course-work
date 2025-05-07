num=int(input("Enter the number: "))
tot_sum=num
while tot_sum>9:
    cur_sum=0
    while num>0:
        cur_sum+=num%10
        num//=10
    tot_sum=cur_sum
    num=cur_sum
print(f'Single digit: {tot_sum}')