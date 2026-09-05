'''
def numbers():
    yield 1
    yield 2
    yield 3

for n in numbers():
    print(n)

def retrivedata():
    data = ['1..100','101...200','201...300','301....400','401....500']
    for i in data:
        yield i

reels = retrivedata()
while True:
    status = input("[s]croll or [q]uit: ")
    if status == 's':
        print(next(reels))
    else:
        break

def retrivedata():
    data = ['1..100', '101...200', '201...300', '301....400', '401....500']
    for i in data:
        yield i

reels = retrivedata()

print(next(reels))
print(next(reels))
print(next(reels))
print(next(reels))
print(next(reels))

def even():
    i = 0
    while True:
        i+=2
        yield i

n = 30
res = even()
for i in range(n):
    print(next(res))

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i
n = int(input("Enter number: "))
for i in factors(n):
    print(i)

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

n=50
res = factors(n)
for i in res:
    print(i)
'''
#prime numbers

def isprimes(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes(n):
    for i in range(2, n + 1):
        if isprimes(i):
            yield i

n = 50
res = primes(n)

for i in res:
    print(i)
    
