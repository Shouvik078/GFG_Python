def second_largest(lst):
    lar=greater_element(lst)
    slar=None
    for i in lst:
        if i!=lar:
            if slar==None:
                slar=i
            else:
                slar=max(slar,i)
    return slar

def greater_element(lst):
    res=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>res:
            res=lst[i]
    return res 

if __name__=='__main__':
    lst=[10,10,20,7,11,9]
    print(greater_element(lst))
    print(second_largest(lst))