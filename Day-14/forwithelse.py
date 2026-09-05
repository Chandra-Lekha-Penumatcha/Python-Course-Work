'''
for i in range(1,10):
    if i==15:
        break
    print(i)

else:
    print("end of the loop")

for i in range(1,10):
    if i==10:
        break
    print(i)
else:
    print("end of the loop")

pin = 1234
for _ in range(5):
    epin = int(input("enter the pin: "))
    if pin == epin:
        print("unlock phone")
        break
    else:
        print("invalid pin")
else:
    print("try again after 30sec.")
    

n = int(input("Enter the number: "))
print("Factors: ",end='')
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')

n = int(input("enter the number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime number")
else:
    print("not prime number")

n = int(input("Enter the number"))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not prime number")
        break
    else:
        print("prime number")
        '''
