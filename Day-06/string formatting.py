Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #splitting and joining methods
>>> c = 'String is immutable'
>>> c.split()
['String', 'is', 'immutable']
>>> 'String, is,immutable'
'String, is,immutable'
>>> 'String, is,immutable'.split()
['String,', 'is,immutable']
>>> 'String, is,immutable'.split(',')
['String', ' is', 'immutable']
>>> 'String, is,immutable'.rsplit(',')
['String', ' is', 'immutable']
>>> s='''
python
programming
lang'''
>>> s
'\npython\nprogramming\nlang'
>>> s.splitlines()
['', 'python', 'programming', 'lang']
>>> ['', 'python', 'programming', 'lang'].join()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    ['', 'python', 'programming', 'lang'].join()
AttributeError: 'list' object has no attribute 'join'
>>> ''.join(['','python', 'programming', 'lang'])
'pythonprogramminglang'
>>> ' '.join(['','python', 'programming', 'lang'])
' python programming lang'
>>> '-'.join(['','python', 'programming', 'lang'])
'-python-programming-lang'
>>> ','.join([1,2,3])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    ','.join([1,2,3])
TypeError: sequence item 0: expected str instance, int found
>>> ','.join(['1','2','3'])
'1,2,3'
>>> 'python.py'.partition('.')
('python', '.', 'py')
>>> s='java,python,c,c++'
>>> s.partition(',')
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
('java,python,c', ',', 'c++')
>>> #whitespace and trimming
>>> c = '        Hello        world            '
>>> c
'        Hello        world            '
>>> c.strip()
'Hello        world'
>>> c.lstrip()
'Hello        world            '
>>> c.rstrip()
'        Hello        world'
>>> #encoding and decoding
>>> text = "Hello "
>>> 
>>> text.encode()
b'Hello '
>>> b'Hello '.decode()
'Hello '
>>> 