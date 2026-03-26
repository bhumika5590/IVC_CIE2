n=int(input("enter a number"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit**3
    n=n//10
if sum==temp:
    print("armstrong number")
else:
    print("not armstrong")