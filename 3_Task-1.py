def factorial(num):
    fact=1
    if (num>0):
        for i in range (1,(num+1)):
            fact=fact*i
        return fact
    elif (num==0):
        return 1
    else:
        print("invalid input")
        return -1
num = int(input("Enter your number: "))
fact1=factorial(num)
if (fact1>0):
    print("Factorial of ",num," is:",fact1)
