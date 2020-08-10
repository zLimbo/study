#### [collections](https://docs.python.org/zh-cn/3/library/collections.html)（容器数据类型）

| name                                                         | introduce                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [namedtuple()](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple) | 创建命名元组子类的工厂函数                                   |
| [deque](https://docs.python.org/zh-cn/3/library/collections.html#collections.deque) | 类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop) |
| [ChainMap](https://docs.python.org/zh-cn/3/library/collections.html#collections.ChainMap) | 类似字典(dict)的容器类，将多个映射集合到一个视图里面         |
| [Counter](https://docs.python.org/zh-cn/3/library/collections.html#collections.Counter) | 字典的子类，提供了可哈希对象的计数功能                       |
| [OrderedDict](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) | 字典的子类，保存了他们被添加的顺序                           |
| [defaultdict](https://docs.python.org/zh-cn/3/library/collections.html#collections.defaultdict) | 字典的子类，提供了一个工厂函数，为字典查询提供一个默认值     |
| [UserDict](https://docs.python.org/zh-cn/3/library/collections.html#collections.UserDict) | 封装了字典对象，简化了字典子类化                             |
| [UserList](https://docs.python.org/zh-cn/3/library/collections.html#collections.UserList) | 封装了列表对象，简化了列表子类化                             |
| [UserString](https://docs.python.org/zh-cn/3/library/collections.html#collections.UserString) | 封装了列表对象，简化了字符串子类化                           |



#### Counter

```python
# 统计英文词频 
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





#### deque

```python
In [1008]: deque(g, 10)
Out[1008]: deque([8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801])
    
# Unix tail 功能
def tail(filename, n=10):
    'Return the last n lines of a fiel'
    with open(filename) as f:
        return deque(f, n)
```



```python
# 轮询调度器
from collections import deque

def roundrobin(*iterables):
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            iterators.popleft()

for task in roundrobin('ABC', 'D', 'EF'):
    print('current task: ', task)
```



#### defaultdict

```python
# 构造图的邻接表

In [1064]: edges = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 4)]

In [1065]: adj = defaultdict(set)

In [1066]: for u, v in edges:
      ...:     adj[u].add(v)
      ...:     adj[v].add(u)
      ...:

In [1067]: adj
Out[1067]: defaultdict(set, {0: {1, 2, 3}, 1: {0, 3}, 2: {0, 4}, 3: {0, 1}, 4: {2}})
```



#### namedtuple

```python
# 赋值 csv, sqlite3 模块返回的元组

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)
```

```python
# _make
In [1071]: Point = namedtuple('Point', ['x', 'y'])

In [1072]: t = [11, 22]

In [1073]: Point._make(t)
Out[1073]: Point(x=11, y=22)
    
# _asdict
In [1074]: p._asdict()
Out[1074]: {'x': 1, 'y': 2}
    
# _fields
In [1075]: Point3D = namedtuple('Point3D', Point._fields + ('z',))
```



```python
# _doc__ 可修改
Book = namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'
```



#### OrderedDict

```python
popitem(last=True)
有序字典的 popitem() 方法移除并返回一个 (key, value) 键值对。 如果 last 值为真，则按 LIFO 后进先出的顺序返回键值对，否则就按 FIFO 先进先出的顺序返回键值对。
```

```python
move_to_end(key, last=True)¶
将现有 key 移动到有序字典的任一端。 如果 last 为真值（默认）则将元素移至末尾；如果 last 为假值则将元素移至开头。如果 key 不存在则会触发 KeyError:

In [1082]: d = OrderedDict.fromkeys('abcde')

In [1083]: d.move_to_end('b')

In [1084]: ''.join(d.keys())
Out[1084]: 'acdeb'

In [1085]: d.move_to_end('b', last=False)

In [1086]: ''.join(d.keys())
Out[1086]: 'bacde'
```

```python
# 实现最新更新
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
```

```python
# 实现 functools.lru_cache()

class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, /, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
```

