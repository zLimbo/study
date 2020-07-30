#### IO编程

> - input/Ouput Stream
> - 同步IO与异步IO，后者效率高，但复杂度远远高于前者
> - IO接口封装了操作系统提供的低级C语言接口

-----

##### 文件操作

- 打开文件

  ```python
  open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
  	'r'       open for reading (default)
      'w'       open for writing, truncating the file first
      'x'       create a new file and open it for writing
      'a'       open for writing, appending to the end of the file if it exists
      'b'       binary mode
      't'       text mode (default)
      '+'       open a disk file for updating (reading and writing)
      'U'       universal newline mode (deprecated)
  ```

  为避免异常，通过`try...finally`确保关闭文件

  ```python
  try:
      f = open('xxx', 'r')
      print(f.read())
  finally:
      if f:
          f.close()
  ```

  `with`语句可自动调用`close()`方法：

  ```python
  with open('xxx', 'r') as f:
      data = f.read()
  print(data)
  ```

- 关闭文件

  ```python
  close() method of _io.TextIOWrapper instance
      Flush and close the IO object.
      
      This method has no effect if the file is already closed.
      
  closed # bool, 文件关闭与否
  ```

- 读文件

  ```python
  # readable()
  readable() method of _io.TextIOWrapper instance
      Return whether object was opened for reading.
  
      If False, read() will raise OSError.
      
  # read
  read(size=-1, /) method of _io.TextIOWrapper instance
      Read at most n characters from stream.
  
      Read from underlying buffer until we have n characters or we hit EOF.
      If n is negative or omitted, read until EOF.
      
  # readline
  readline(size=-1, /) method of _io.TextIOWrapper instance
      Read until newline or EOF.
  
      Returns an empty string if EOF is hit immediately.
      
  # readlines
  readlines(hint=-1, /) method of _io.TextIOWrapper instance
      Return a list of lines from the stream.
  
      hint can be specified to control the number of lines read: no more
      lines will be read if the total size (in bytes/characters) of all
      lines so far exceeds hint.
  ```

- 写文件

  ```python
  # writable
  writable() method of _io.TextIOWrapper instance
      Return whether object was opened for writing.
  
      If False, write() will raise OSError.
  
  # write
  write(text, /) method of _io.TextIOWrapper instance
      Write string to stream.
      Returns the number of characters written (which is always equal to
      the length of the string).
  
  # writelines
  writelines(lines, /) method of _io.TextIOWrapper instance
      Write a list of lines to stream.
  
      Line separators are not added, so it is usual for each of the
      lines provided to have a line separator at the end.
      
  # flush
  flush() method of _io.TextIOWrapper instance
      Flush write buffers, if applicable.
  
      This is not implemented for read-only and non-blocking streams.
      
  # truncate
  truncate(pos=None, /) method of _io.StringIO instance
      Truncate size to pos.
  
      The pos argument defaults to the current file position, as
      returned by tell().  The current file position is unchanged.
      Returns the new absolute position.
  ```

- 文件属性

  ```python
  f.name
  f.encoding
  f.mode
  
  # fileno
  fileno() method of _io.TextIOWrapper instance
      Returns underlying file descriptor if one exists.
  
      OSError is raised if the IO object does not use a file descriptor.
  ```

- 文件指针

  ```python
  # tell
  tell() method of _io.TextIOWrapper instance
      Return current stream position.
      
  # seek
  seek(cookie, whence=0, /) method of _io.TextIOWrapper instance
      Change stream position.
  
      Change the stream position to the given byte offset. The offset is
      interpreted relative to the position indicated by whence.  Values
      for whence are:
  
      * 0 -- start of stream (the default); offset should be zero or positive
      * 1 -- current stream position; offset may be negative
      * 2 -- end of stream; offset is usually negative
  
      Return the new asolute position.
  ```

------

##### file-like Object

> `open`函数返回有个`read()`方法的对象在Python中统称为`file-like Object`，除了file外，还可以是内存字节流，网络流，自定义流，不用特定类继承，只需要`read()`方法

- StringIO

  ```python
  from io import StringIO
  f = StringIO()
  f.write('hello') # 5
  f.write('world!') # 6
  f.getvalue() # 'hello world!'
  
  f2 = StringIO('Hello\nHi!\nGoodbye!')
  while True:
      s = f2.readline()
      if s == '':
          break
      print(s.strip())
  ```

- BytesIO

  ```python
  from io import BytesIo
  f = BytesIO()
  f.write('中文'.encode('utf-8')) # 6
  f.getvalue() # b'\xe4\xb8\xad\xe6\x96\x87'
  
  f2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
  f2.read() # b'\xe4\xb8\xad\xe6\x96\x87'
  ```

- 操作文件和目录

  > 复制文件并非由操作系统提供的系统调用
  >
  > 详见os模块
  
  ```python
  # 在某目录下查找含有字符的文件
  import os
  import sys
  
  def find(path, s):
      for basename in os.listdir(path):
          p = os.path.join(path, basename)
          if os.path.isdir(p):
              find(p, s)
          elif s in basename:
              print(os.path.relpath(p, '.'))
  
  def find2(path, s):
      for dirpath, dirnames, filenames in os.walk(path):
          for filename in filenames:
              if s in filename:
                  abspath = os.path.join(dirpath, filename)
                  relpath = os.path.relpath(abspath, '.')
                  yield relpath
  
  if __name__ == '__main__':
      path, s = sys.argv[1], sys.argv[2]
      print('find {} in {}:'.format(s, path))
      for path in find2(path, s):
          print(path)
  ```
  
  ```python
  # ls -l
  import os
  import sys
  import time
  
  def ls(path):
      files = os.listdir(path)
      for file in files:
          p = os.path.join(path, file)
          t = os.path.getmtime(p)
          t_str = time.strftime('%m月 %d %H:%M ', time.localtime(t)) + file
          if os.path.isdir(p):
              t_str += '/'
          print(t_str)
  
  if __name__ == '__main__':
      path = sys.argv[1]
      ls(path)
  ```
  
  

