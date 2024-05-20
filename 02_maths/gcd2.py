def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


if __name__=='__main__':
    a=int(input("Enter a number :"))
    b=int(input("Enter a number :"))
    print(gcd(a,b))

