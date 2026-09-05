'''n = int(input("enter a number"))
for i in range(1, 11):
    print(n, "x", i,  "=", n * i)


    


n = int(input("Enter the number: "))
print(n * 55)
#common is 55

num = int(input("Enter a number: "))
n = num
reversed_num = 0

while n != 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n = n // 10

print("Reversed Number:", reversed_num)

print("Prime numbers between 1 and 100:")

count = 0

for num in range(2, 101):
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
        count += 1

print("\n\nTotal Prime Numbers:", count)

start = int(input("Enter a start number: "))
end = int(input("Enter an end number: "))

for n in range(start, end + 1):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        print(n)
'''
text = input("Enter a string: ")

vow = 0
cons = 0

for ch in text:
    ch = ch.lower()
    if ch.isalpha():
        if ch in "aeiou":
            vow += 1
        else:
            cons += 1

print("Vowels:", vow)
print("Consonants:", cons)