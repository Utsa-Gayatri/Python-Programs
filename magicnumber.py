a=int(input("Enter a number : "))
sum=a
n=a
while(sum>9):
    n=sum
    sum=0
    while n>0:
        w=n%10
        sum+=w
        n=n//10

if sum==1:
    print("Magic Number")
else:
    print("Not a Magic Number")
