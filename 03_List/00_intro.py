# List is dynamic array 

# Allows different types of item (int,str)

# we use square bracket [] 

lst =[11,5,2,7,9] # index start from zero 

print(lst)
print(lst[0])

print(lst[-1])

lst.append(23)   # it will append 23 in last of the lst 
print(lst)

lst.insert(1,15) # 15 will be insert in 1st index
print(lst)

# checking 7 present in lst or not   ans :   True/False

print(7 in lst)

# count of occurence of 2 
print(lst.count(2))

# using index function - u can get any number's first occurence index, if not present in list it will give error

print(lst.index(7))

# lst,index(n,start,end)

print(lst.index(9,4,6))













