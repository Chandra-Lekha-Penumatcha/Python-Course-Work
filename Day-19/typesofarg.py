#four types of arguments: positional,keyword,positional
#mapping is done according to position of arguments called as positional arguments
'''
def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')
display('xyz', 'xyz@gmail.com', 'xyz@123')
display('xyz123', 'xyz@gmail.com','xyz')
display('xyz@gmail.com', 'xyz123', 'xyz')

def display(name,email,password):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display(name='xyz', email='xyz@gmail.com',password= 'xyz@123')
display(password='xyz123', email='xyz@gmail.com',name='xyz')
display(email='xyz@gmail.com', password='xyz123', name='xyz')
#default arguments: If no value is passed during the function call, the default value is used.

def display(name,email='gmail.com',password=''):
    print(f'name: {name}')
    print(f'email: {email}')
    print(f'password: {password}')

display('xyz', 'xyz@gmail.com', 'xyz@123')
display('xyz', 'xyz@gmail.com')
display('xyz')

#vairable-positional -single 
def display(*names):
    print(names)
display('sajid')
display('sajid','abdul')
display('sajid','abdul','dheeraj')
display('sajid','abdul','vikas')

def display(**products):
    print(products)

display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)
'''
