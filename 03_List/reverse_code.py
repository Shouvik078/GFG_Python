def reverselist(lst):
    s=0
    e=len(lst)-1
    while s<e:
        lst[s],lst[e]=lst[e],lst[s]
        s+=1
        e-=1
    return lst 

if __name__=='__main__':
    lst=[2,3,5,7,11]
    print(reverselist(lst))