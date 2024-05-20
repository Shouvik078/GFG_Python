def lcm(a,b):
    res=max(a,b)
    
    while True:
        if res%a==0 and res%b==0:
            return res 
        res+=1
    
    return res


if __name__=='__main__':
    a=int(input("Enter a number :"))
    b=int(input("Enter a number :"))
    print(lcm(a,b))