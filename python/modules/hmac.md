#### hmac.new

```python
new(key, msg=None, digestmod='')
Create a new hashing object and return it.

key: bytes or buffer, The starting key for the hash.
msg: bytes or buffer, Initial input for the hash, or None.
digestmod: A hash name suitable for hashlib.new(). *OR*
           A hashlib constructor returning a new hash object. *OR*
           A module supporting PEP 247.

Required as of 3.8, despite its position after the optional
msg argument.  Passing it as a keyword argument is
recommended, though not required for legacy API reasons.

You can now feed arbitrary bytes into the object using its update()
method, and can ask for the hash value at any time by calling its digest()
or hexdigest() methods.
```

#### hmac.digest

```python
digest(key, msg, digest)
    Fast inline implementation of HMAC.

    key: bytes or buffer, The key for the keyed hash object.
    msg: bytes or buffer, Input message.
    digest: A hash name suitable for hashlib.new() for best performance. *OR*
            A hashlib constructor returning a new hash object. *OR*
            A module supporting PEP 247.
等价于 hmac.new(key, msg, digestmod).digest()
```

#### hmac.compare_digest(a, b)

> 返回 a == b。 此函数使用一种经专门设计的方式通过避免基于内容的短路行为来防止定时分析，使得它适合处理密码。 a 和 b 必须为相同的类型：或者是 str (仅限 ASCII 字符，如 HMAC.hexdigest() 的返回值)，或者是 bytes-like object。
> 注解 如果 a 和 b 具有不同的长度，或者如果发生了错误，定时攻击在理论上可以获取有关 a 和 b 的类型和长度信息 — 但不能获取它们的值。



#### hmac.HMAC

```python
class HMAC(builtins.object)
 |  HMAC(key, msg=None, digestmod='')
 |
 |  RFC 2104 HMAC class.  Also complies with RFC 4231.
 |
 |  This supports the API for Cryptographic Hash Functions (PEP 247).
 |
 |  Methods defined here:
 |
 |  __init__(self, key, msg=None, digestmod='')
 |      Create a new HMAC object.
 |
 |      key: bytes or buffer, key for the keyed hash object.
 |      msg: bytes or buffer, Initial input for the hash or None.
 |      digestmod: A hash name suitable for hashlib.new(). *OR*
 |                 A hashlib constructor returning a new hash object. *OR*
 |                 A module supporting PEP 247.
 |
 |                 Required as of 3.8, despite its position after the optional
 |                 msg argument.  Passing it as a keyword argument is
 |                 recommended, though not required for legacy API reasons.
 |
 |  copy(self)
 |      Return a separate copy of this hashing object.
 |
 |      An update to this copy won't affect the original object.
 |
 |  digest(self)
 |      Return the hash value of this hashing object.
 |
 |      This returns the hmac value as bytes.  The object is
 |      not altered in any way by this function; you can continue
 |      updating the object after calling this function.
 |
 |  hexdigest(self)
 |      Like digest(), but returns a string of hexadecimal digits instead.
 |
 |  update(self, msg)
 |      Feed data from msg into this hashing object.
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |
 |  name
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  blocksize = 64
```



```python
# hmac登录
import hmac
import random

def hmac_md5(key, msg):
    return hmac.new(key.encode('utf-8'), msg.encode('utf-8'), 'MD5').hexdigest()

class User:
    def __init__(self, name, passwd):
        self.name = name
        self.key = ''.join([chr(random.randint(48, 122)) for _ in range(20)])
        self.passwd = hmac_md5(self.key, passwd)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, passwd):
    user = db[username]
    return user.passwd == hmac_md5(user.key, passwd)

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```

