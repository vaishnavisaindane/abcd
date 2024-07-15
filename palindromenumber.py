n=int(input("enter your number"))
copy=n
rev=0
while n>0:
    z=n%10
    rev=rev*10+z
    n=n//10
print(rev)
if copy == rev:
    print("palindrome")
else:
    print("not a palindrome")
