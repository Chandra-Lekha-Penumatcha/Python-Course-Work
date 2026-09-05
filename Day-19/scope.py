#global variable can be acessed in both inside and outside
#local variable can only be acessed in inside 
#declare global it will effect both inside and outside #do not require pass the function
#global - A variable declared outside all functions is called a global variable.
'''
def display():
    n=10
    print('Inside:', n)

def display():
    display(n)
    print('Outside:', n)

def display(n):
    n=n+10
    print('Inside:',n)

n=10
display(n)
print('Outside:',n)

def display():
    print('Inside:',n)
   
n=10
display()
print('Outside:',n)
 
def display():
    n=10
    print('Inside:',n)

display()
print('Outside:',n)

def display():
    global n
    n=n+10
    print('Inside:',n)

n=10
display()
print('Outside:',n)


def display():
    global n
    n='PFS'
    print("Updated Course:",n)
n = JFS
display()
print("Final Course:",n)

#nonlocal -it is used to effect only inside the function
def display():
    n = 'JFS'
    def update():
        nonlocal n
        n='PFS'
        print("Updated course:",n)
    update()
    print("Final Course:",n)
display()
'''
#built in methods
#when we declare a built in function sum becomes variable instead of function
l = [1,2,3,4,5]
max=20
sum = 10
print(sum)