def left_non_rep(s):
    char=256
    count=[0]*char
    for i in s:
        count[ord(i)]+=1
    for i in range(len(s)):
        if count[ord(s[i])]==1:
            return i
    return -1
          

s='abccecbad'
print(left_non_rep(s))

