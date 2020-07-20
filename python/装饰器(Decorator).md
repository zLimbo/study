#### 装饰器(Decorator)

> 在代码运行期间动态增加函数功能且不修改函数定义的方式成为装饰器(decorator)，其本质是一个返回函数的高阶函数。



##### 创建装饰器

```python
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```



##### @语法

```python
@log
def now():
    print('2020-07-19')
```

相当于执行了 `now = log(now)`，`now`变量指向了新的函数，即`log(now)`返回的`wrapper(*args, **kw)`, 其接受任意参数的调用。



##### decorator本身需要传入参数

```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
        return func(*args, **kw)
    return wrapper
return decorator
```

使用：

```python
@log('execute')
def now():
    print('2020-07-19')
```

等价于：

```python
now = log('execute')(now)
```

`log('execute')`返回`decorator(func)`函数，最后返回`warpper(*args, **kw)`函数。

##### 保留原函数属性

经过上文的装饰，`now.__name__`成为`'warpper'`，须将原函数的`__name__`等属性复制到新函数中，否则依赖函数签名的代码执行会出错。

可使用内置的`functools.wraps`进行相关操作：

```python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
```

```python
import functools

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
```



```python
# 函数运行前后装饰

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        ret = func(*args, **kw)
        print('end call')
        return ret
    return wrapper
```



```python
# 有参数与无参数装饰

import functools

def log(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    if callable(arg):
        text = "call"
        return decorator(arg)
    elif isinstance(arg, str):
        text = arg
        return decorator
    else:
        raise TypeError('input error')
```

