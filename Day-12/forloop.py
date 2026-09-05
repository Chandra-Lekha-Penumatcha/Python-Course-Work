#str list tuple set dict range()
seq = [10, 20, 30, 40]

for var in seq:
    print(var)

s= 'codegnan'
for ch in s:
    if ch in 'aeiouAEIOU':
        print(ch)

l = [10,13,23,45,67,78,89]
for i in l:
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")
'''
marks = (90,30,40,60,90,70)
for mark in marks:
    if mark>35:
        print(mark,"pass")
    else:
        print(mark,"fail")
    
'''
followers = {"chandra","vaishu","suhitha","amrutha","gayathri","lasya"}
for i in followers:
    print(i)
bus = {'s1':'booked','s2':'available','s3':'available','s4':'booked','s5':'available'}
for seat in bus:
    if bus.get(seat) == 'available':
        print(seat, bus.get(seat))
#range(start,end+1,step) => (0,nodef,1)=>default value
for i in range(1, 11):
    print(i)
for i in range(2,51,2):
    print(i,end=' ')

for i in range(1,100,2):
    print(i,end=' ')
n= int(input("Enter the table no: "))
for i in range(1,11):
    print(f'{n} * {i} = {n*i}')
    
 