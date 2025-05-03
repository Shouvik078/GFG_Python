def left_most_duplicate(s):
    char=256
    visited=[False]*256
    res=-1
    for i in range(len(s)-1,-1,-1):
        if visited[ord(s[i])]==True:
            res=i
        else:
            visited[ord(s[i])]=True
    return res 

s='abcbd'
print(left_most_duplicate(s))

