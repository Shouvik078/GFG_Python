def isPrime(n):
    for i in range (2,n):
        if n%i==0:
            return False
        
    return True 

def pFactors(n):
    for i in range (2,n+1):
        if isPrime(i):
            x=i
            while n%x==0:
                print(i)
                x=x*i
            
if __name__=='__main__':
    n=int(input("Enter a number : "))
    print(pFactors(n))