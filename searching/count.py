def first_occur(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if x>l[mid]:
            low=mid+1
        elif x<l[mid]:
            high=mid-1
        else:
            if mid==0 or l[mid]!=l[mid-1]:
                return mid
            else:
                high=mid-1
    return -1
    
def last_occur(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if x>l[mid]:
            low=mid+1
        elif x<l[mid]:
            high=mid-1
        else:
            if len(l)-1==mid or l[mid]!=l[mid+1]:
                return mid
            else:
                low=mid+1
    return -1
            

def count_occur(l,x):
    first=first_occur(l,x)
    if first==-1:
        return -1
    else:
        return last_occur(l,x)-first+1


l=[10,20,20,30,40]
x=20
# print(first_occur(l,x))
# print(last_occur(l,x))
# print(count_occur(l,x))

def count_one(l1,x1):
    n=len(l1)-1
    first=first_occur(l1,x1)
    return n-1-first


l1=[0,0,0,0,1,1,1,1,1,1,1,1,1]
x1=1
print(count_one(l1,x1))