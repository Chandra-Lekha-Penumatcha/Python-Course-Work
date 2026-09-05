n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum =", sum)

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits =", sum)

n = int(input("Enter a number: "))

count = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        count = count + 1

print("Count =", count)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

numbers = [a, b, c]
maximum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i
print("Maximum =", maximum)

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

n = int(input("Enter a number: "))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum == n:
    print("perfect")
else:
    print("not perfect")

n = int(input("Enter a number: "))
count = 0
while n > 0:
    count = count + 1
    n = n // 10
print("Digits =", count)

n = int(input("enter a number: "))
for i in range(1, n + 1):
    if i % 7 == 0:
        print(i)

a = int(input("Enter first number: "))
b = int(input("enter second number: "))

lcm = max(a, b)
while True:
    if lcm % a == 0 and lcm % b == 0:
        print("LCM =", lcm)
        break
    lcm = lcm + 1

n = int(input("Enter a number: "))

while n >= 1:
    if n % 2 == 0:
        print(n)
    n = n - 1

n = int(input("Enter a number: "))
sum = 0
for i in range(1, 2 * n, 2):
    sum = sum + i
print("Sum =", sum)

n = int(input("Enter a number: "))

temp = n
count = len(str(n))
sum = 0

for i in str(n):
    digit = int(i)
    sum = sum + digit ** count

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")

n = int(input("Enter the size: "))

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()