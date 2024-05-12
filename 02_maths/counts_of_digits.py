n=int(input("Enter a number : "))
s=n 
t=0
while(n>0):
    t=t+1
    n=n//10
print("Total digits in",s,"are :",t)