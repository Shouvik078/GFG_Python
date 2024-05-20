def isPal(n):
    rev=0
    temp=n
    while temp!=0:
        ld=temp%10
        rev=rev*10+ld
        temp//=10
    return rev==n 
        

if __name__=='__main__':
    n=int(input("Enter a number : "))
    print(isPal(n))