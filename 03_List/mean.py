def average(lst):
    sum=0
    for i in lst:
        sum+=i
    n=len(lst)
    return sum/n


if __name__=='__main__':
    lst=[11,9,7,4,13]
    print("Mean of list is :",average(lst))