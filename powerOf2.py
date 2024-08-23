inputNum = int(input("Enter the number:"))

if inputNum <= 0:
    print(inputNum, "is not a power of 2")
else:
    while inputNum % 2 == 0:
        inputNum = inputNum / 2
    if inputNum == 1:
        print(f"The number  is a power of 2")
    else:
        print("The number is not a power of 2")