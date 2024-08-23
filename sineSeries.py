import math
def sin(x,n):
    s=0
    for i in range(n):
        p=(2*i+1)
        sign=(-1)**i
        pi=22/7
        y=(x*pi)/180
        s = s + ((y**(p))/math.factorial(p))*sign
    return s
x=int(input("Enter the value of x in degrees:"))
n=int(input("Enter the number of terms:"))
print(round(sin(x,n),2))