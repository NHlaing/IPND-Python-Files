 s = '<any string>'
 s[3], s[1+ 1 + 1]
('y', 'y')
>>> s[0], (s + s)[0]
('<', '<')
>>> s[0] + s[1], s[0 + 1]
('<a', 'a')
>>> s[1], (s + 'ity')[1]
('a', 'a')
>>> s[-1], (s + s)[-1]
('>', '>')
>>> sentence = 'Working on the wall is hazardous."
SyntaxError: EOL while scanning string literal
>>> sentence = 'Working on the wall is hazardous.'
>>> print sentence[3:]
king on the wall is hazardous.
>>> print 'moutain' sentence[11:]
SyntaxError: invalid syntax
>>> print 'mountain ' + sentence[11:] + "!" *5
mountain the wall is hazardous.!!!!!
>>> print sentence[11:] + 'mountain' + "!" * 4
the wall is hazardous.mountain!!!!
>>> print sentence[:11] +'mountain'
Working on mountain
>>> d = 'Everyone can attain Navana.'
>>> print d[:8]+'could' + d
EveryonecouldEveryone can attain Navana.
>>> print d.find('can')
9
>>> print d[9:]
can attain Navana.
>>> c ='can attain Navana.'
>>> print 'By following the eight fought parth everyone' = c
SyntaxError: invalid syntax
>>> print 'By following the eight fought parth everyone' + c
By following the eight fought parth everyonecan attain Navana.
>>> A ='By following the eight fought parth everyonecan attain Navana.'
>>> print A.find[13:]

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print A.find[13:]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
>>> print A.find('eight')
17
>>> print A[17:]
eight fought parth everyonecan attain Navana.
>>> print A.find('Z')
-1
>>>
>>>
>>> s.find(s)
0
>>> s.find('s')
5
>>> 's'.find('s')
0
>>> s.find('')
0
>>> s.find(s + '!!!') + 1
0
>>>
