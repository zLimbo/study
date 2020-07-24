##### Object Oriented Programming

> - OOP是一种程序设计思想，将对象作为编程基本单元，其包含数据和函数，与之相对的是POP(Procedure Oriented Programming)，将函数作为基本单元。
> - 每个对象都可以接受其他对象发来的消息，然后处理这些消息，计算机执行就是一系列 消息在各个对象间传递。
> - 三个特性：抽象、继承、多态
> - Python中一切数据类型皆是对象。

##### 类和实例（抽象）

> - 类是抽象的模板，实例是根据类创建的一个个具体对象，每个对象方法相同，但数据可能不同，之间相互独立
> - 方法是与实例绑定的函数
> - 实例可独自创建非共有的数据成员（因为Python是动态语言可以在运行时创建变量）

##### 访问限制（封装）

> - `__xxx`是私有变量，外部不能访问。一般解释器将其变为`_Obj__xxx`（不同解释器可能不同），故仍可通过`_Obj__xxx`访问
> - `__xxx__`是特殊变量，可直接访问，不是`private`变量
> - `_xxx`约定不能随意访问
> - 在`class`定义外新增`__xxx`不会成为私有变量

##### 继承和多态

> - 继承基类的方法
> - 若子类重新定义基类方法，将覆盖基类方法
> - 开闭原则：
>   - 对扩展开放：允许新增子类
>   - 对修改封闭：不需要修改依赖基类的相关函数，子类可直接做为参数
> - 动态语言的“鸭子类型”：在运行时判断类型，故即使不是某类的子类，但拥有和其相同的方法，就可以使用依赖前者的函数（静态在编译器判断类型进而报错）

##### 获取对象信息

> - `isinstance(obj, class_or_tuple, /)` 判断一个对象是否是某种类型
>
> - `type(object)` 函数判断对象类型
>
> - `types` 模块提供函数类型供判断：
>
>   ```python
>   import types
>   
>   def fn():
>       pass
>   
>   # 以下皆为 True
>   type(fn) == types.FunctionType
>   type(abs) == types.BuiltinFunctionType
>   type(lambda x: x) == types.LambdaType
>   type((x for x in range(10))) == types.GeneratorType
>   ```
>
> - `dir()`获得一个类或对象的所有属性和方法
>
> - `getattr()`, `setattr()`, `hasattr()` 可直接操作一个对象的状态
>
>   ```python
>   hasattr(obj, 'x')			# 是否有 x 属性, 属性须通过双引号访问
>   hasattr(obj, '__init__')	# 是否有 __init__ 属性
>   getattr(obj, 'x')			# 获得 x 属性，没有则抛出 AttributeError 错误
>   getattr(obj, 'z', 404)		# 获得 z 属性, 不存在则返回 404
>   setattr(obj, 'y', "123")	# 添加属性 y 为 "123"
>   
>   def readImage(fp):
>       if hasattr(fp, 'read'):
>           return readData(fp)
>       return None
>   ```

#####  实例属性和类属性

> - 实例属性和类属性互不干扰
> - 类属性属于类，所有实例共享（访问时为`Obj.xxx`）

##### `__slots__`

>- 动态绑定方法
>
>  给实例绑定方法：
>
>  ```python
>  import types
>  
>  class Student:
>      pass
>  
>  def set_age(self, age):
>      self.age = age
>  
>  s = Student()
>  s.set_age = types.MethodType(set_age, s)
>  s.set_age(25)
>  ```
>
>  > 仅对该实例有效，对其他实例无效
>
>  给类绑定方法：
>
>  ```python
>  Student.set_score = set_score
>  s1 = Student()
>  s2 = Student()
>  s1.set_age(20)
>  s2.set_age(21)
>  ```
>
>- 使用 `__slots__` 限制实例的属性
>
>  ```python
>  class Student(object):
>      __slots__ = ('name', 'age')		# 元组定义允许绑定的属性名称
>      
>  s = Student()
>  s.sex = 'male'	# 抛出 AttributeError 错误
>  ```
>
>  当前类的 `__slots__` 对子类继承无效

##### `@property` 

> 为了保护实例数据和检查其是否符合规范，通常提供 `set_xxx()` 方法设置数据，`get_xxx()` 方法获取数据，但这样比较复杂。`Python`内置的`@property`装饰器负责将一个方法变成属性调用。
>
> 把一个`getter`方法变成属性只需要加上`@property`，同时`@property`本身又创建了另一个装饰器`@xxx.setter`，负责把一个`setter`方法变成属性赋值。
>
> ```python
> class Student(object):
>     @property
>     def score(self):
>         rturn self._score
>     
>     @score.setter
>     def score(self, value):
>         if not isinstance(value, int):
>             raise ValueError('score must be integer!')
>         if value < 0 or value > 100:
>             raise ValueError('score must between 0~100!')
>         self._score = value
>         
> s = Student()
> s.score = 60	# 实际转化为 s.set_score(60)
> s.score			# 实际转化为 s.get_score()
> ```
>
> 例子
>
> ```python
> class Screen(object):
>     
>     @property
>     def width(self):
>         return self._width
>         
>     @width.setter
>     def width(self, width):
>         if not isinstance(width, int):
>             raise ValueError('width must be integer!')
>         if width < 0:
>             raise ValueError('width must be greater than 0 !')
>         self._width = width
>         
>     @property
>     def height(self):
>         if not isinstance(width, int):
>             raise ValueError('width must be integer!')
>         if width < 0:
>             raise ValueError('width must be greater than 0 !')
>         return self._height
>         
>     @height.setter
>     def height(self, height):
>         self._height = height
>     
>     @property
>     def resolution(self):
>         return self._width * self._height
> ```

##### 多重继承

> - `MixIn`：在主线单一继承外的额外功能继承功能，如：
>
>   编写一个多进程的TCP服务:
>
>   ```python
>   class MyTCPServer(TCPServer, ForkingMixIn):
>       pass
>   ```
>
>   编写一个多线程模式的UDP服务，定义如下：
>
>   ```python
>   class MyUDPServer(UDPServer, ThreadMinIn):
>       passs
>   ```
>
>   编写一个协程模型：
>
>   ```python
>   class MyTCPServer(TCPServer, CoroutinMixIn):
>       pass
>   ```

##### 定制类

> 特殊用途的 `__xxx__` 属性
>
> - `__slots__` 限定类属性
>
> - `__len__()` 让类作用于 `len()` 函数
>
> - `__str__()` 让类作用于 `str()` 函数，也是`print()`后的内容
>
> - `__repr__()` 返回程序开*+发者能看到的字符串，服务于调试
>
> - `__iter__()` 让类作用于`for ... in ..`循环，该方法返回一个迭代对象，`for`循环会不断调用该迭代对象的`__next__()`方法拿到下一个值，直至遇到`StopIteration`异常退出循环。
>
>   ```python
>   class Fib(object):
>   
>       def __init__(self, n):
>           self.__n = n
>           self.__a = 0
>           self.__b = 1
>           self.__cur = 0
>   
>       def __iter__(self):
>           return self
>   
>       def __next__(self):
>           if self.__cur >= self.__n:
>               raise StopIteration
>           self.__cur += 1
>           ret = self.__a
>           self.__a, self.__b = self.__b, self.__a + self.__b
>           return ret
>       
>       def __len__(self):
>           return self.__n - self.__cur
>           
>       def __str__(self):
>           return 'The first %d Fibonacci Numbers.' % self.__n
>           
>       __repr__ = __str__
>       
>   fib = Fib(10)
>   print(fib)
>   print(repr(fib))
>   for i in fib:
>       print(i)
>   ```
>
>   
>
> - `__getitem__()`  让类能通过`[]`获取元素
>
> - `__getattr__()` 在类未找到相关属性时，就会调用该函数。利用这个方法可将类的属性和方法动态化处理，如链式调用：
>
>   ```python
>   class Chain(object):
>       
>       def __init__(self, path=''):
>           self._path = path
>           
>       def __getattr__(self, path):
>           return Chain('%s/%s' % (self._path, path))
>       
>       def __call__(self, path):
>           return Chain('%s/%s' % (self._path, path))
>       
>       def __str__(self):
>           return self._path
>       
>       __repr__ = __str__
>       
>   print(Chain().status.user.timeline.list)
>   # /status/user/timeline/list
>   print(Chain().user('zlimbo').repos)
>   # /user/zlimbo/repos
>   ```
>
> - `__call__()` 可对实例进行调用
>
>   ```python
>   class Fib(object):
>       def __call__(self, n):
>           a, b = 0, 1
>           while n > 0:
>               a, b = b, a + b
>               n -= 1
>           return a
>       
>   fib = Fib()
>   print(callable(fib))  # True
>   print(fib(10))
>   ```

##### `enum`(枚举类)

> ```python
> from enum import Enum
> 
> Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
> 
> for name, member in Month.__members__.items():
>     print(name, '=>', member, ',', member.value)
> ```
>
> `value`属性是自动赋给成员的`int`常量，默认从1开始计数
>
> 可从`Enum`派生出自定义类：
>
> ```python
> from enum import Enum, unique
> 
> @unique
> class Weekday(Enum):
>     Sun = 0
>     Mon = 1
>     Tue = 2
>     Wed = 3
>     Thu = 4
>     Fri = 5
>     Sat = 6
> ```
>
> `@unique`装饰器检查有无重复值
>
> 访问：
>
> ```python
> Weekday.Mon
> Weekday['Tue']
> Weekday.Wed.value
> Weekday(4)
> Weekday.__members__
> ```
>
> `Enum` 把一组相关常量定义在一个`class`中，且`class`不可变，且成员间可以比较

##### 动态创建类

> - `type(object_or_name, bases, dict)` 
>
>   ```python
>   def fn(self, name='world'):
>       print('Hello, %s' % name)
>   
>   Hello = type('Hello', (object,), dict(hello=fn))
>   print(type(Hello)) 
>   # <class 'type'>
>   ```
>
>   通过`type()`函数创建的类和直接写`class`是完全一样的，因为`Python`解释器遇到`class`定义时，仅仅是扫描`class`定义的语法，然后调用`type()`函数创建出`class`。
>
> - `metaclass` （元类）
>
>   元类是类的定义模板，可以创建类或修改类。其实是`type`的派生类，重新定义创建规则。
>
>   ```python
>   class TestMixin(object):
>       def test(self):
>           print('This is TestMixin.test')
>   
>   class ListMetaclass(type):
>       def __new__(cls, name, bases, attrs):
>           print('This is ListMetaclass.__new__')
>           print("cls:", str(cls))
>           print("name:", str(name))
>           print("bases:", str(bases))
>           print("attrs:", str(attrs))
>           attrs['add'] = lambda self, value: self.append(value)
>           return type.__new__(cls, name, bases, attrs)
>       
>   class MyList(list, TestMixin, metaclass=ListMetaclass):
>       def __init__(self):
>           print('This is MyList.__init__')
>   
>   L = MyList()
>   L.add(1)	# 普通的list没有add方法
>   print(L)
>   L.test()
>   ```
>
>   ```shell
>   # 输出为：
>   This is ListMetaclass.__new__
>   cls: <class '__main__.ListMetaclass'>
>   name: MyList
>   bases: (<class 'list'>, <class '__main__.TestMixin'>)
>   attrs: {'__module__': '__main__', '__qualname__': 'MyList', '__init__': <function MyList.__init__ at 0x00000247165A1820>}
>   This is MyList.__init__
>   [1]
>   This is TestMixin.test
>   ```
>
>   当类继承参数传入关键词参数`metaclass`时，它指示`Python`解释器在创建`MyList`时，就通过`ListMetaclass.__new__()`来创建。
>
>   `__new__()`方法接受的参数依次为：元类名称；类的名字；类继承的集合；类的方法集合。
>
>   **元类应用**
>
>   `ORM` （Object Relational Mapping，对象关系映射），即把关系数据库的一行映射为一个对象，一个类对应一个表，便于代码编写而无须`SQL`语句。编写一个`ORM`框架，所有的类只能动态定义，因为只有使用者才能根据表的结构定义对应的类。
>
>   ```python
>   # User表到User类的映射
>   class User(Model):
>       #定义类的属性到列的映射
>       id = IntegerField('id')
>       name = StringField('username')
>       email = StringField('email')
>       password = StringField('password')
>       
>   # 创建一个实例
>   user = User(id=1234, name='test', email='test@orm.org', password='testpwd')
>   # 保存到数据库
>   user.save()
>   ```
>
>   父类`Model`和属性`StringField`, `IntegerField` 由`ORM`框架提供，其他的魔术方法如`save()`全部由`metaclass`自动完成。
>
>   一个简单的`ORM`实现如下：
>
>   ```python
>   # 先定义Field类
>   class Field(object):
>       """Field类负责保存数据库表的字段名和字段类型"""
>   
>       def __init__(self, name, column_type):
>           self.name = name
>           self.column_type = column_type
>           
>       def __str__(self):
>           return '<%s:%s>' % (self.__class__.__name__, self.name)
>   
>   # 再派生各种类型的Field类
>   class StringField(Field):
>   
>       def __init__(self, name):
>           super(StringField, self).__init__(name, 'varchar(100)')
>   
>   class IntegerField(Field):
>   
>       def __init__(self, name):
>           super(IntegerField, self).__init__(name, 'bigint')
>   
>   # 元类 ModelMetaclass类
>   class ModelMetaclass(type):
>   
>       def __new__(cls, name, bases, attrs):
>           if name == 'Model':
>               return type.__new__(cls, name, bases, attrs)
>           print('Found model: %s' % name)
>           mappings = dict()
>           for k, v in attrs.items():
>               if isinstance(v, Field):
>                   print('Found mapping: %s ==> %s' % (k, v))
>                   mappings[k] = v
>           attrs.clear()
>           attrs['__mappings__'] = mappings # 保存属性和列的映射关系
>           attrs['__table__'] = name
>           return type.__new__(cls, name, bases, attrs)
>   
>   # 基类 Model
>   class Model(dict, metaclass=ModelMetaclass):
>   
>       def __init__(self, **kw):
>           super(Model, self).__init__(**kw)
>   
>       def __getattr__(self, key):
>           try:
>               return self[key]
>           except KeyError:
>               raise AttributeError(r"'Model' object has no attribte '%s'" % key)
>   
>       def __setattr__(self, key, value):
>           slef[key] = value
>   
>       def save(self):
>           fields = []
>           params = []
>           args = []
>           for k, v in self.__mappings__.items():
>               fields.append(v.name)
>               params.append('?')
>               args.append(getattr(self, k, None))
>           sql = 'INSERT INTO %s (%s) VALUES (%s)' % (self.__table__, ','.join(fields), ','.join(params))
>           print('SQL: %s' % sql)
>           print('FIELDS: %s' % str(fields))
>           print('ARGS: %s' % str(args))
>   
>   # User表到User类的映射，User类自动继承基类的元类
>   class User(Model):
>       #定义类的属性到列的映射
>       id = IntegerField('id')
>       name = StringField('username')
>       email = StringField('email')
>       password = StringField('password')
>       
>   # 创建一个实例
>   user = User(id=1234, name='test', email='test@orm.org', password='testpwd')
>   # 保存到数据库
>   user.save()
>   ```
>
>   ```python
>   # 输出
>   Found model: User
>   Found mapping: id ==> <IntegerField:id>
>   Found mapping: name ==> <StringField:username>
>   Found mapping: email ==> <StringField:email>
>   Found mapping: password ==> <StringField:password>
>   SQL: INSERT INTO User (id,username,email,password) VALUES (?,?,?,?)
>   FIELDS: ['id', 'username', 'email', 'password']
>   ARGS: [1234, 'test', 'test@orm.org', 'testpwd']
>   ```

