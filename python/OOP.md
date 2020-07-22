#### Object Oriented Programming

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

#### `@property` 

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

