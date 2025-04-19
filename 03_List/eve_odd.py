def check_even_odd(lst):
    even=[]
    odd=[]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

if __name__=='__main__':
    lst=[11,9,6,4,13]
    print(check_even_odd(lst))
    
