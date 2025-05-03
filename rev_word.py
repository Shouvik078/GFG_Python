def rev_str(s):
    revv=''
    s1=s.split()
    for i in range(len(s1)-1,-1,-1):
        revv=revv+s1[i]
    return revv

s='I love coding'
print(rev_str(s))

