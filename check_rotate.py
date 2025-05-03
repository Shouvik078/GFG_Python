s1='abcd'
s2='cdab'

s3=s1+s1
# print(s2 in s3)

def isRotate(s1,s2):
    if len(s1)!=len(s2):
        return False
    temp=''
    temp=s1+s1
    return temp.find(s2)!=-1


sin1=input('Enter first string : ')
sin2=input('Enter second string : ')

print(isRotate(sin1,sin2))
