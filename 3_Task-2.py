import math
def mathmodule(num):
    if num>=0:
        print("Square root of ",num,"is:",math.sqrt(num))
    else:
        a=math.sqrt(num*-1)
        b=str(a)
        c=b+' i'
        print("Square root of ",num,"is:",c)
    if num>0:
        print("Logarithm of ",num,"is:",math.log(num))
    else:
        print("Logithm of ",num,"is: Not defined")
    print("Sine of ",num,"is:",math.sin(num))
num=int(input("Enter a number: "))
mathmodule(num)


