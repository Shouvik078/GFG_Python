'''
s1={10,30,20}
print(s1)
print(type(s1))

s2=set([35,40,15])
print(s2)
print(type(s2))

s3=set()
print(s3)
print(type(s3))


s1={10,20}
print(s1)
s1.add(30)
print(s1)

s1.update([40,50])
print(s1)
s1.update([60,70],[30,15])
print(s1)


s={10,20,30,40,50}
print(s)
s.discard(20)
print(s)


difference between remove and discard 
discard will not through error if element is not present in set,
remove will through error if element is present in set.

s.remove(50)
print(s)
s.clear()
print(s)

'''

s1={2,4,6,8}
s2={3,6,9}

print(s1|s2)
print(s1&s2)

print(s1-s2)
print(s1^s2)
