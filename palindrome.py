def checkPalindrome(l):
    start=0
    end=len(l)-1
    while end>start:
        if l[start]!=l[end]:
            return False
        start+=1
        end-=1
    return True


l=input('Enter a string : ')
print(checkPalindrome(l))

# sol 2
if l==l[::-1]:
    print('Yes')
else :
    print('No')
