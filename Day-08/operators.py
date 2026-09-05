Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=20
>>> b=10
>>> a+b
30
>>> a-b
10
>>> a*b
200
>>> a/b
2.0
>>> 9/2
4.5
>>> a//b
2
>>> a**b
10240000000000
>>> 4**2
16
>>> 9%2
1
>>> a
20
>>> b
10
>>> a<b
False
>>> a>b
True
>>> a<=b
False
>>> a>=b
True
>>> a==b
False
>>> a!=b
True
>>> c=10
>>> c=c+10
>>> c
20
>>> c=c+10
>>> c
30
>>> c=c+10
>>> c
40
>>> c += 10
>>> c *= 2
>>> c
100
>>> c //= 2
>>> c
50
>>> c **= 2
>>> c
2500
>>> c %= 3
>>> c
1
>>> c /= 2
>>> c
0.5
>>> True and True
True
>>> n = 10
>>> n%2==0
True
>>> n%3==0
False
>>> n%2==0 and n%3==0
False
>>> n%2==0 or n%3==0
True
>>> n%8==0 or n%3==0
False
>>> n
10
>>> n<5
False
>>> not n<5
True
>>> not n>5
False
>>> #str list tuple set dict
>>> s='codegyan'
>>> 'e' in s
True
>>> 'm' in s
False
>>> 'd' in s
True
>>> l=[1,2,3,4]
>>> 4 in l
True
>>> 8 in l
False
>>> 2 in l
True
>>> t=(5,6,7,8)
>>> 5 in t
True
>>> 7 in t
True
>>> 2 in t
False
>>> s={1,2,5,6}
>>> 2 in s
True
>>> 6 in s
True
>>> 8 in s
False
>>> d=['name':'likitha', 'batch': 63, 'course': 'python']
SyntaxError: invalid syntax
>>> d={'name': 'likitha','batch':63,'course':'python'}
>>> 'name' in d
True
>>> 'likitha' in d
False
>>> 63 in d
False
>>> 'python' in d
False
>>> 'course' in d
True
>>> l=[1,2,3,4]
>>> m=[1,2,3,4]
>>> id(l)
1884819482176
>>> id(m)
1884787993856
>>> l is m
False
>>> n = l
>>> id(n)
1884819482176
>>> l is n
True
>>> l is not m
True
>>> l is not n
False
>>> #mutable amd immutable
>>> a+=10
>>> a
30
>>> id(a)
1884777639120
>>> s={1,2,3,4}
>>> id(s)
1884819570976
>>> s.add(5)
>>> s
{1, 2, 3, 4, 5}
>>> id(s)
1884819570976
>>> s = 'codegnan'
>>> id(s)
1884819618864
>>> s ='codegnan courses'
>>> id(s)
1884819561008
>>> #bitwise
>>> 9&10
8
>>> 9|10
11
>>> 9^10
3
>>> 8>>2
2
>>> 8<<2
32
>>> ~8
-9
>>> ~45
-46
>>> ~56
-57
>>> #output
>>> a = 10
>>> b = 10.5
>>> c = 'codegyan'
>>> print(a,b,c)
10 10.5 codegyan
>>> print("a value is ",a)
a value is  10
>>> print("a value is",a"|b value is",b"| c value is",c )
SyntaxError: invalid syntax
>>> print("a value is",a|"b value is",b|" c value is",c )
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print("a value is",a|"b value is",b|" c value is",c )
TypeError: unsupported operand type(s) for |: 'int' and 'str'
>>> print(a,b,c,sep='')
1010.5codegyan
>>> print(a,b,c,sep='\n')
10
10.5
codegyan
>>> print(a,b,c,sep='\t')
10	10.5	codegyan
>>> print(a,b,c,sep='\t',end='@')
10	10.5	codegyan@
>>> print(a,b,c,sep='\t',end='\n\n')
10	10.5	codegyan

>>> #recommended area
>>> print(f'a={a} b={b} c={c}')
a=10 b=10.5 c=codegyan
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.500000 c=codegyan
>>> 
>>> print('a=%d b=%2f c=%s'%(a,b,c))
SyntaxError: invalid syntax
>>> print('a ={} | b ={} | c ={}'.format(a,b,c))
a =10 | b =10.5 | c =codegyan
>>> print('a ={} | b ={} | c ={}'.format(c,a,b))
a =codegyan | b =10 | c =10.5
>>> print('a ={2} | b ={0} | c ={1}'.format(a,b,c))
a =codegyan | b =10 | c =10.5
>>> 