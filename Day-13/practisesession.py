num = int(input("Enter a number: "))
if num>0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("zero")


num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")



num = int(input("enter a number: "))

if num % 5 == 0:
    print("divisible by 5")
else:
    print("Not divisible by 5")

num = int(input("enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")

year = int(input("enter a year: "))
if (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")

num = int(input("enter the marks: "))
if num >= 35:
    print("pass")
else:
    print("fail")

ch = input("enter a character: ")
vowels = "aeiou"
for i in vowels:
    if ch == i:
        print("vowel")
        break
    else:
        print("not a vowel")

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num1 > num2:
    print(num1, "is greater")
elif num2 > num1:
    print(num2, "is greater")
else:
    print("both numbers are equal")


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num1 < num2:
    print(num1, "is smaller")
elif num2 > num1:
    print(num2, "is smaller")
else:
    print("both numbers are equal")

num = int(input("enter a number: "))
if num == 0:
    print("Number is zero")
else:
    print("not a zero")

num = int(input("enter a number: "))
if num % 10 ==0:
    print("multiple of 10")
else:
    print("not multiple of 10")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

num = int(input("Enter a number: "))

if 1 <= num <= 100:
    print("In range")
else:
    print("Out of range")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2 * num2:
    print(num1, "is square of", num2)
else:
    print(num1, "is not square of", num2)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are not equal")

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("Positive and even number")
else:
    print("Not a positive and even number")

ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase letter")
else:
    print("Not an uppercase letter")

temp = int(input("Enter temperature: "))

if temp > 30:
    print("It's hot")
else:
    print("It's not hot")