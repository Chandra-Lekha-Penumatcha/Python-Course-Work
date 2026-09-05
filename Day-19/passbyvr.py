#passing by values are immutable
#passing by reference are mutable
#list set dict-mutable
#int float str tuple bool-immutable 
#int float str list tuple set dict bool

def display(n):
    n[5]=6
    print("Inside:",n)
n ={1:2,3:4}
display(n)
print('Outside:',n)


    