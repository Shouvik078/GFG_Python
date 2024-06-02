def get_smaller(lst,x):
    return [e for e in lst if e<x]

if __name__=='__main__':
    lst=[9,11,4,7,12,18]
    x=10
    print(get_smaller(lst,x))
    
