'''
def checkSub(s1,s2):
    i,j=0,0
    while(i<len(s1) and j<len(s2)):
        if s1[i]==s2[j]:
            j=j+1
        i=i+1
    if j==len(s2):
        return True
    return False

s1='abcde'
s2='de'
print(checkSub(s1,s2))

'''

def rec_sub(s1,s2,m,n):
    if n==0:
        return True
    if m==0:
        return False
    if s1[m-1]==s2[n-1]:
        return rec_sub(s1,s2,m-1,n-1)
    if s1[m-1]!=s2[n-1]:
        return rec_sub(s1,s2,m-1,n)

s1='abcde'
s2='de'
m=len(s1)
n=len(s2)

print(rec_sub(s1,s2,m,n))
