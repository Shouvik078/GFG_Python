'''
def chekk(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                return False
    return True
'''

def chekk(lst):
    i=1
    while i<len(lst):
        if lst[i]<lst[i-1]:
            return False
        i+=1
    return True

if __name__=='__main__':
    lst=[10,20,20,30,10]
    print(chekk(lst))