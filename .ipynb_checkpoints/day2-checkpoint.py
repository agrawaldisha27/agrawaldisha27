Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello'+' '+'world'
'hello world'
a='python'
b='ghgh'
id(a)
2176974436144
id(b)
2176975275632
a='computer'
id(a)
2176975218416
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
len(keyword.kwlist)
35
a_1='hii'
bool(1)
True
bool(0)
False
bool(True)
True
bool(False)
False
print"M_C"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#a=200
a=20
b=20
a,b,c=20.20,40
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a,b,c=20.20,40
ValueError: not enough values to unpack (expected 3, got 2)
a,b,c=20,20,20
a=b=c=20
print(c)
20
2//=3
SyntaxError: 'literal' is an illegal expression for augmented assignment
3/=2
SyntaxError: 'literal' is an illegal expression for augmented assignment
a//=
SyntaxError: invalid syntax
a//=6
print(a)
3
a and b
20
a=2
b=4
a and b
4
'''hello'''
'hello'
my_tuple=(1,2,3,4,5)
type(my_list)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    type(my_list)
NameError: name 'my_list' is not defined
type (my_tuple)
<class 'tuple'>
print(t)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(t)
NameError: name 't' is not defined
print(my_tuple)
(1, 2, 3, 4, 5)
d={'div':'pop'}
bool("hooii")
True
bool(None)
False
