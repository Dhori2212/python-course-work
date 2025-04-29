def calculate(price,rate,time):
    sum=(price*rate*time)%100
    return sum
price=float(input("Enter the price"))
rate=float(input("Enter the rate"))
time=float(input("Enter the time"))
re= calculate(price,rate,time)
print(re)