


n = int(input("enter your number:"))
flag = False
for i in range(2,11):
    if(n%i==0):
        flag = True
        break

if(flag==True):
    print("not prime")
else:
    print("prime")