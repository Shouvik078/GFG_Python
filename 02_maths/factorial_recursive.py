def rec_fact(n):
    if n==0:
        return 1
    return n*rec_fact(n-1)

if __name__=='__main__':
    n=int(input("Enter a number : "))
    print("Factorial of",n,"is :",rec_fact(n)) 