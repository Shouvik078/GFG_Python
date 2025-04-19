'''
d1={101:'abc',102:'mno',103:'xyz'}
print(d1)
print(d1[101])


d={}
print(d)
print(type(d))
d['Laptop']=58000
d['Monile']=78000
d['Watch']=1100
print(d)
print(d['Monile'])


d1={101:'abc',102:'mno',103:'xyz'}
print(d1[101])
print(d1.get(101))
print(d1.get(122))
print(d1.get(122),"Not present")
'''

d={101:'abc',102:'mno',103:'xyz'}
d[101]='Shouvik'
print(d)
# remove key value pair - but gives value
print(d.pop(101))
print(d)
# another way to delete - delete both
del d[103]
print(d)
d[108]='Insert'
# to get last inserted value 
print(d.popitem())



