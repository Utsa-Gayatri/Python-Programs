def factorial(n):
          if(n==1):
            return 1
          else:
            fac=n*factorial(n-1)
            return fac
    
num=int(input("Enter a number : "))
result=factorial(num)
print("Factorial = ",result)