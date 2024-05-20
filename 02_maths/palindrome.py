n=int(input("Enter a number : "))
chk=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10

if rev==chk:
    print("Palindrome")
else :
    print("Not Palindrom") 