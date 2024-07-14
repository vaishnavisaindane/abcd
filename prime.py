#prime
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
  if n==1 :
    print("not prime neither composite")
    break
  elif n%i==0 :
    count=count+1
if count==2:
  print("prime")
else:
  print("not prime")
