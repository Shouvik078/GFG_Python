def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a 

if __name__=='__main__':
    a=int(input("Enter the value of a :")) 
    b=int(input("Enter the value of b :"))
    
    print(gcd(a,b))