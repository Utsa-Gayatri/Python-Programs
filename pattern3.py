rows = int(input("Enter number of rows: "))
w = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            w = 1
        else:
            w = w * (i - j)//j
        print(w, end = " ")
    print()