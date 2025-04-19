def greater_element(lst):
    res=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>res:
            res=lst[i]
    return res 

if __name__=='__main__':
    lst=[11,3,6,7,17,21,4]
    print(greater_element(lst))
    print(max(lst))
    print(min(lst))