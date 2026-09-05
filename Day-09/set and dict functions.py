Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #set and dict
>>> s = {}
>>> type(s)
<class 'dict'>
>>> s=set()
>>> s={1,2,3,5,67,89,356,768}
>>> s
{768, 1, 2, 67, 3, 5, 356, 89}
>>> s=set()
>>> s
set()
>>> s.add(2)
>>> s.add(13.8)
>>> s.add(3+5j)
>>> s
{2, (3+5j), 13.8}
>>> s={1,1,1,1,1}
>>> s
{1}
>>> c={10,20,30}
>>> d={5,6,7,8}
>>> c+d
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c+d
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> a={1,2,3,4,5}
>>> b={3,5,7,9}
>>> a
{1, 2, 3, 4, 5}
>>> b
{9, 3, 5, 7}
>>> a | b
{1, 2, 3, 4, 5, 7, 9}
>>> a & b
{3, 5}
>>> a - b
{1, 2, 4}
>>> a ^ b
{1, 2, 4, 7, 9}
>>> {1}<=a
True
>>> {1,2,3,4}<=a
True
>>> a
{1, 2, 3, 4, 5}
>>> {1,2,3,4,5}<=a
True
>>> {4,5}<=a
True
>>> a
{1, 2, 3, 4, 5}
>>> b
{9, 3, 5, 7}
>>> a.isdisjoint(b)
False
>>> a.isdisjoint({8,9})
True
>>> a.union(b)
{1, 2, 3, 4, 5, 7, 9}
>>> a.intersection(b)
{3, 5}
>>> a.issubset(b)
False
>>> a.issuperset(b)
False
>>> a
{1, 2, 3, 4, 5}
>>> 4 in a
True
>>> 2 in a
True
>>> 7 not in a
True
>>> b
{9, 3, 5, 7}
>>> 3 in b
True
>>> 10 not in b
True
>>> a
{1, 2, 3, 4, 5}
>>> max(a)
5
>>> min(a)
1
>>> sorted(a)
[1, 2, 3, 4, 5]
>>> sum(a)
15
>>> a
{1, 2, 3, 4, 5}
>>> b=a
>>> b
{1, 2, 3, 4, 5}
>>> b.add(12)
>>> b
{1, 2, 3, 4, 5, 12}
>>> a
{1, 2, 3, 4, 5, 12}
>>> c = a.copy()
>>> c.add(12)
>>> c.add(14)
>>> c
{1, 2, 3, 4, 5, 12, 14}
>>> a
{1, 2, 3, 4, 5, 12}
>>> a.add(456)
>>> a
{1, 2, 3, 4, 5, 456, 12}
>>> #update function
>>> a.update({15,16,17})
>>> a
{1, 2, 3, 4, 5, 456, 12, 15, 16, 17}
>>> a.pop()
1
>>> a.pop()
2
>>> a
{3, 4, 5, 456, 12, 15, 16, 17}
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.remove()
TypeError: set.remove() takes exactly one argument (0 given)
>>> #remove function
>>> a.remove(456)
>>> a.remove(16)
>>> a
{3, 4, 5, 12, 15, 17}
>>> a.discard(16)
>>> a.discard(456)
>>> a
{3, 4, 5, 12, 15, 17}
>>> a.clear()
>>> a
set()
>>> #frozenset
>>> a = frozenset({1,16,17,47,52,34})
>>> a
frozenset({16, 1, 34, 17, 52, 47})
>>> a.add(15)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.add(15)
AttributeError: 'frozenset' object has no attribute 'add'
>>> #dict function
>>> d={}
>>> d=dict{}
SyntaxError: invalid syntax
>>> d=dict()
>>> type(d)
<class 'dict'>
>>> d= {'k1':'v1','k2':'v2','k3':'v3'}
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
>>> id(d)
2461011398272
>>> d['k4'] ='v4'
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
>>> d['k5'] = 'v4'
>>> d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v4'}
>>> d['k1'] = 'v11'
>>> d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v4'}
>>> d={}
>>> d[1]='int'
>>> d
{1: 'int'}
>>> d[14.7]='float'
>>> d
{1: 'int', 14.7: 'float'}
>>> d['str']='string'
>>> d
{1: 'int', 14.7: 'float', 'str': 'string'}
>>> d[(1,2,3,4)]='tuple'
>>> d
{1: 'int', 14.7: 'float', 'str': 'string', (1, 2, 3, 4): 'tuple'}
>>> d[4+5j]='complex'
>>> d
{1: 'int', 14.7: 'float', 'str': 'string', (1, 2, 3, 4): 'tuple', (4+5j): 'complex'}
>>> d={}
>>> d[1]=1
>>> d[2]=14.8
>>> d[3]=3+5j
>>> d[4]='str'
>>> d[5]=[1,2,3,4]
>>> d[6]=(1,2,3)
>>> d[7]={1,2,3}
>>> d[8]={1:1}
>>> d[9]=True
>>> d
{1: 1, 2: 14.8, 3: (3+5j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> 8 in d
True
>>> 11 in d
False
>>> d[5]
[1, 2, 3, 4]
>>> d[9]
True
>>> d[3]
(3+5j)
>>> d.get(10)
>>> d.get(2)
14.8
>>> d.get(11,"key is not present")
'key is not present'
>>> d.get(5,"key is not present")
[1, 2, 3, 4]
>>> #update function
>>> d
{1: 1, 2: 14.8, 3: (3+5j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=14
>>> d
{1: 1, 2: 14.8, 3: 14, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[5]=18
>>> d
{1: 1, 2: 14.8, 3: 14, 4: 'str', 5: 18, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=24
>>> d
{1: 1, 2: 14.8, 3: 14, 4: 'str', 5: 18, 6: 24, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 14.8, 3: 14, 4: 'str', 5: 18, 6: 24, 7: 20, 8: {1: 1}, 9: True}
>>> 