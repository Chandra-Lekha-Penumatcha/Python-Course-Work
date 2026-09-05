'''
def isleapyear(year):
    if year%400 ==0 or (year%4==0 and year%100!=0):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not leap year")
for year in range(2001,2027):
    isleapyear(year)


def display(name, email, password):
    print("Name:", name)
    print("Email:", email)
    print("Password:", password)

display("Chandra Lekha", "lekha@gmail.com", "12345")
display("vaishu", "vaishu@gmail.com", "1234")
display("suhitha", "suhi@gmail.com", "123456")

def sumofdigits(n):
    sum = 0
    while n>0:
        sum += n%10
        n=n//10
    return sum
n = int(input("Enter the number: "))
print(f'sum of {n} digits is {sumofdigits(n)}')

def productofdigits(n):
    pro = 1
    while n>0:
        pro *= n%10
        n=n//10
    return pro
n = int(input("Enter the number: "))
print(f'Product of {n} digits is {productofdigits(n)}')

def checkpassword(password):
    if len(password) > 8:
        check = set()
        for i in password:
            if i.isupper():
                check.add('u')
            elif i.islower():
                check.add('l')
            elif i.isdigit():
                check.add('d')
            else:
                check.add('s')
        if len(check) == 4:
            return "Strong Password"
    return "Weak Password"
    
password = input("Enter password: ")
print(checkpassword(password))


def table(n):
    print(f'----------Table- {n}------------')
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
for i in range(1,21):
    table(i)
'''
