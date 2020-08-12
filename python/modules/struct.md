### 函数

#### struct.pack

```python
struct.pack(format, v1, v2, ...)
返回一个 bytes 对象，其中包含根据格式字符串 format 打包的值 v1, v2, ... 参数个数必须与格式字符串所要求的值完全匹配。
```

#### struct.pack_into

```python
struct.pack_into(format, buffer, offset, v1, v2, ...)
根据格式字符串 format 打包 v1, v2, ... 等值并将打包的字节串写入可写缓冲区 buffer 从 offset 开始的位置。 请注意 offset 是必需的参数。
```

#### struct.unpack

```python
struct.unpack(format, buffer)
根据格式字符串 format 从缓冲区 buffer 解包（假定是由 pack(format, ...) 打包）。 结果为一个元组，即使其只包含一个条目。 缓冲区的字节大小必须匹配格式所要求的大小，如 calcsize() 所示。
```

#### struct.unpack_from

```python
struct.unpack_from(format, buffer, offset=0)
对 buffer 从位置 offset 开始根据格式字符串 format 进行解包。 结果为一个元组，即使其中只包含一个条目。 缓冲区的字节大小从位置 offset 开始必须至少为 calcsize() 显示的格式所要求的大小。
```

#### struct.iter_unpack

```python
struct.iter_unpack(format, buffer)
根据格式字符串 format 以迭代方式从缓冲区 buffer 解包。 此函数返回一个迭代器，它将从缓冲区读取相同大小的块直至其内容全部耗尽。 缓冲区的字节大小必须整数倍于格式所要求的大小，如 calcsize() 所示。

每次迭代将产生一个如格式字符串所指定的元组。
```

#### struct.calcsize

```python
struct.calcsize(format)
返回与格式字符串 format 相对应的结构的大小（亦即 pack(format, ...) 所产生的字节串对象的大小）。
```



### 格式字符串

> 格式字符串是用来在打包和解包数据时指定预期布局的机制。 它们使用指定被打包/解包数据类型的 [格式字符](https://docs.python.org/zh-cn/3/library/struct.html#format-characters) 进行构建。 此外，还有一些特殊字符用来控制 [字节顺序，大小和对齐方式](https://docs.python.org/zh-cn/3/library/struct.html#struct-alignment)。

#### 字节顺序，大小和对齐方式

| 字符 | 字节顺序      | 大小     | 对齐方式 |
| :--- | :------------ | :------- | :------- |
| `@`  | 按原字节      | 按原字节 | 按原字节 |
| `=`  | 按原字节      | 标准     | 无       |
| `<`  | 小端          | 标准     | 无       |
| `>`  | 大端          | 标准     | 无       |
| `!`  | 网络（=大端） | 标准     | 无       |

如果第一个字符不是其中之一，则假定为 `'@'` 。

#### 格式字符

> 格式字符具有以下含义；C 和 Python 值之间的按其指定类型的转换应当是相当明显的。 ‘标准大小’列是指当使用标准大小时以字节表示的已打包值大小；也就是当格式字符串以 `'<'`, `'>'`, `'!'` 或 `'='` 之一开头的情况。 当使用本机大小时，已打包值的大小取决于具体的平台。

| 格式 | C 类型               | Python 类型       | 标准大小 | 注释     |
| :--- | :------------------- | :---------------- | :------- | :------- |
| `x`  | 填充字节             | 无                |          |          |
| `c`  | `char`               | 长度为 1 的字节串 | 1        |          |
| `b`  | `signed char`        | 整数              | 1        | (1), (2) |
| `B`  | `unsigned char`      | 整数              | 1        | (2)      |
| `?`  | `_Bool`              | bool              | 1        | (1)      |
| `h`  | `short`              | 整数              | 2        | (2)      |
| `H`  | `unsigned short`     | 整数              | 2        | (2)      |
| `i`  | `int`                | 整数              | 4        | (2)      |
| `I`  | `unsigned int`       | 整数              | 4        | (2)      |
| `l`  | `long`               | 整数              | 4        | (2)      |
| `L`  | `unsigned long`      | 整数              | 4        | (2)      |
| `q`  | `long long`          | 整数              | 8        | (2)      |
| `Q`  | `unsigned long long` | 整数              | 8        | (2)      |
| `n`  | `ssize_t`            | 整数              |          | (3)      |
| `N`  | `size_t`             | 整数              |          | (3)      |
| `e`  | (6)                  | float             | 2        | (4)      |
| `f`  | `float`              | float             | 4        | (4)      |
| `d`  | `double`             | float             | 8        | (4)      |
| `s`  | `char[]`             | 字节串            |          |          |
| `p`  | `char[]`             | 字节串            |          |          |
| `P`  | `void *`             | 整数              |          | (5)      |

```python
# 获得BNP头信息
# -*- coding: utf-8 -*-
import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAA' +
                   'AAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3/' +
                   '/f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/A' +
                   'HwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9' +
                   '//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f' +
                   '/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHw' +
                   'AfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//' +
                   '38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9' +
                   '//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAf' +
                   'AB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHw' +
                   'AfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//' +
                   '3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')

from collections import namedtuple
BMPHeader = namedtuple('BMPHeader', ('type1', 'type2', 'size', 'keep1', 'offset', 
    'header_size', 'width', 'height', 'keep2', 'color_num'))

def bmp_info(data):
    header = BMPHeader._make(struct.unpack('<ccIIIIIIHH', data[:30]))
# 输出：
# BMPHeader(type1=b'B', type2=b'M', size=616, keep1=0, offset=54, header_size=40, width=28, height=10, keep2=1, color_num=16)
#
```



```python
In [1131]: struct.pack('hhl', 1, 2, 3)
Out[1131]: b'\x01\x00\x02\x00\x03\x00\x00\x00'

In [1132]: struct.unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
Out[1132]: (256, 512, 50331648)

In [1133]: struct.unpack('>hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
Out[1133]: (1, 2, 3)

In [1134]: struct.calcsize('hhl')
Out[1134]: 8
```



```python
In [1135]: record = b'raymond   \x32\x12\x08\x01\x08'

In [1136]: name, serialnum, school, gradelevel = struct.unpack('<10sHHb', record)

In [1137]: name, serialnum, school, gradelevel
Out[1137]: (b'raymond   ', 4658, 264, 8)

In [1138]: Student = namedtuple('Student', 'name serialnum school gradelevel')

In [1139]: Student._make(struct.unpack('<10sHHb', record))
Out[1139]: Student(name=b'raymond   ', serialnum=4658, school=264, gradelevel=8)
```



```python
In [1143]: struct.pack('ci', b'*', 0x12131415)
Out[1143]: b'*\x00\x00\x00\x15\x14\x13\x12'

In [1144]: struct.pack('ic', 0x12131415, b'*')
Out[1144]: b'\x15\x14\x13\x12*'

In [1145]: struct.calcsize('ci')
Out[1145]: 8

In [1146]: struct.calcsize('ic')
Out[1146]: 5
```



```python
In [1147]: struct.pack('llh0l', 1, 2, 3)
Out[1147]: b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
```



### 类

#### struct.Struct(*format*)

```python
# 方法
pack
pack_into
unpack
unpack_from
iter_unpack
format
size
```



```python
In [1160]: struct.Struct('llh')
Out[1160]: <Struct at 0x2cd22e13f70>

In [1161]: s = struct.Struct('llh')

In [1162]: s.size
Out[1162]: 10

In [1163]: s.format
Out[1163]: 'llh'

In [1164]: s.pack(1,2,3)
Out[1164]: b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00'

In [1165]: s.unpack(b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00')
Out[1165]: (1, 2, 3)
```

