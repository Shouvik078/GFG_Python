def get_res(l):
    even=[e for e in l if e%2==0]
    odd=[e for e in l if e%2!=0]
    return even,odd

if __name__=='__main__':
    l=[5,11,2,3,14,6,18,9]
    even,odd=get_res(l)
    print(even,'\n',odd)