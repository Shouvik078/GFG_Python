# Count of number frequency 

def cnt_fre(arr,n):
    hmp=dict()
    for i in range(n):
        if arr[i] in hmp.keys():
            hmp[arr[i]]+=1
        else:
            hmp[arr[i]]=1
    for i in hmp:
        print(i, ' ', hmp[i])


lst=[50,50,10,40,10]
n=len(lst)
print(cnt_fre(lst,n)) 