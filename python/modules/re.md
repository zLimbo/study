

#### re.compile

```python
compile(pattern, flags=0)
    Compile a regular expression pattern, returning a Pattern object.
```



#### re.search

```python
search(pattern, string, flags=0)
    Scan through string looking for a match to the pattern, returning
    a Match object, or None if no match was found.
```



#### re.match

```python
match(pattern, string, flags=0)
    Try to apply the pattern at the start of the string, returning
    a Match object, or None if no match was found.
```



#### re.fullmatch

```python
fullmatch(pattern, string, flags=0)
    Try to apply the pattern to all of the string, returning
    a Match object, or None if no match was found.
```



#### re.split

```python
split(pattern, string, maxsplit=0, flags=0)
    Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list.
```

```python
In [377]: re.split(r'\W+','今天，没有雨，没有风,热')
Out[377]: ['今天', '没有雨', '没有风', '热']

In [378]: re.split(r'(\W+)','今天，没有雨，没有风,热')
Out[378]: ['今天', '，', '没有雨', '，', '没有风', ',', '热']
 
In [381]: re.split(r'\W*','今天，没有雨，没有风,热')
Out[381]: ['', '今', '天', '', '没', '有', '雨', '', '没', '有', '风', '', '热', '']

In [379]: re.split('[a-f]+', '0a3B9', flags=re.I)
Out[379]: ['0', '3', '9']
```



#### re.findall

```python
findall(pattern, string, flags=0)
    Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result.
```

```python
In [971]: with open('test/py/test_decorator.py') as f:      
     ...:     words = re.findall(r'\w+', f.read().lower())  
     ...: Counter(words).most_common(10)                    
     ...:                                                   
Out[971]:                                                   
[('print', 4),                                              
 ('def', 3),                                                
 ('func', 3),                                               
 ('return', 3),                                             
 ('test', 3),                                               
 ('functools', 2),                                          
 ('log', 2),                                                
 ('wrapper', 2),                                            
 ('args', 2),                                               
 ('kw', 2)]                                                 
```



#### re.finditer

```python
finditer(pattern, string, flags=0)
    Return an iterator over all non-overlapping matches in the
    string.  For each match, the iterator returns a Match object.

    Empty matches are included in the result.
```

```python
In [383]: g = re.finditer('a', 'abababababab')

In [384]: for i in g:
     ...:     print(i)
     ...:
<re.Match object; span=(0, 1), match='a'>
<re.Match object; span=(2, 3), match='a'>
<re.Match object; span=(4, 5), match='a'>
<re.Match object; span=(6, 7), match='a'>
<re.Match object; span=(8, 9), match='a'>
<re.Match object; span=(10, 11), match='a'>
```



#### re.sub

```python
sub(pattern, repl, string, count=0, flags=0)
    Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used.
```

```python
In [387]: re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
     ...:         r'static PyObject*\npy_\1(void)\n{',
     ...:         'def myfunc():')
Out[387]: 'static PyObject*\npy_myfunc(void)\n{'
    
In [388]: def dashrepl(matchobj):
     ...:     if matchobj.group(0) == '_': return ''
     ...:     else: return '-'
     ...:

In [389]: re.sub('-{1,2}', dashrepl, 'pro----gram-files')
Out[389]: 'pro--gram-files'    
```



#### re.subn

```python
subn(pattern, repl, string, count=0, flags=0)
    Return a 2-tuple containing (new_string, number).
    new_string is the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in the source
    string by the replacement repl.  number is the number of
    substitutions that were made. repl can be either a string or a
    callable; if a string, backslash escapes in it are processed.
    If it is a callable, it's passed the Match object and must
    return a replacement string to be used.
```

