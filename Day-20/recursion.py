'''
def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)


def display(n):
    if n<1:
        return
    print(n)
    display(n-1)

display(10)

def displaysum(n):
    if n==0:
        return 0
    return n+displaysum(n-1)
print(displaysum(8))

#factorial
def displaymult(n):
    if n==0:
        return 0
    return n*displaymult(n-1)
print(displaymult(8))

#multiplication
def multiply(n):
    if n == 1:
        return 1
    return n*multiply(n - 1)

print(multiply(5))

def display(n):
    if n == 0:
        return
    print('python programming')
    display(n - 1)
display(5)

def display(ind):
    if ind == len(s):
        return
    print(s[ind])
    display(ind+1)
s = 'Python Programming'
display(0)

def display(ind):
    if ind == len(s):
        return
    print(s[ind],end=' ')
    display(ind+1)

s = 'Python Programming'
display(0)


def display(ind):
    if ind == len(s):
        return
    print(s[:ind + 1])
    display(ind + 1)
s = 'Python'
display(0)

def display(ind):
    if ind > len(s):
        return
    print(s[:n])
    display(n+1)
s = 'Python'
display(1)

def display(ind):
    if ind >= len(s):
        return
    print(s[ind:ind+4])
    display(ind+4)

s = "python"
display(0)

def display(ind,w):
    if ind > len(s) - w:
        return
    print(s[ind:ind+w])
    display(ind+1,W)
s= 'python programming'
display(0,10)

#using Recursion display it as digits 


def display(n):
    if n == 0:
        return
    display(n // 10)
    print(n % 10)
display(987654)

#sumofdigits

def sumdigits(n):
    if n == 0:
        return 0
    return n % 10 + sumdigits(n // 10)

print(sumdigits(987654))
#prepare upto functions and python script
#technologies asked in linkedin job profiles upto 50 companies
'''
#fibbanoci series
a = 0
b = 1
n = 10
for i in range(n-1):
    a,b = b,a+b
    print(b)
#using recursion
