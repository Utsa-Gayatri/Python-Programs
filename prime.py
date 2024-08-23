n=int(input("Enter a number :"))
i=2
f=0
while i<n:
    if n%i==0:
        f=1 
        break
    else:
        i=i+1

if f==0 :
    print("Prime Number")
else:
    print("Not a Prime Number")