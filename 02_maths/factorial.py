def factorial(n):
    res=1
    for i in range (2,n+1):
        res=res*i
    return res

if __name__=='__main__':
    n=int(input("Enter number to see factorial : "))
    print("Factorial of",n,"is :",factorial(n)) 