## Square root technique

def isPrime(n):
    if n==1 or n%2==0:
        return False
    if n==2 or n==3:
        return True
    i=5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False 
        i+=6
    return True
    

if __name__=='__main__':
    n=int(input("Checking prime or not : "))
    print("Prime Number") if isPrime(n) else print("Not Prime numbers")


