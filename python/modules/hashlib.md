```python
In [11]: dir(hashlib)
Out[11]:
['algorithms_available',
 'algorithms_guaranteed',
 'blake2b',
 'blake2s',
 'md5',
 'new',
 'pbkdf2_hmac',
 'scrypt',
 'sha1',
 'sha224',
 'sha256',
 'sha384',
 'sha3_224',
 'sha3_256',
 'sha3_384',
 'sha3_512',
 'sha512',
 'shake_128',
 'shake_256']
```

```python
md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(), sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256.
  
class HASH(builtins.object)
 |  HASH(name, string=b'')
 |
 |  A hash is an object used to calculate a checksum of a string of information.
 |
 |  Methods:
 |
 |  update() -- updates the current digest with an additional string
 |  digest() -- return the current digest value
 |  hexdigest() -- return the current digest as a string of hexadecimal digits
 |  copy() -- return a copy of the current hash object
 |
 |  Attributes:
 |
 |  name -- the hash algorithm being used by this object
 |  digest_size -- number of bytes in this hashes output
 |
 |  Methods defined here:
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  copy(self, /)
 |      Return a copy of the hash object.
 |
 |  digest(self, /)
 |      Return the digest value as a bytes object.
 |
 |  hexdigest(self, /)
 |      Return the digest value as a string of hexadecimal digits.
 |
 |  update(self, obj, /)
 |      Update this hash object's state with the provided string.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  block_size
 |
 |  digest_size
 |
 |  name
```

##### 通用用法

```python
In [15]: md5.update('ab'.encode('utf-8'))

In [16]: md5.digest()
Out[16]: b'\x18~\xf4Ca"\xd1\xcc/@\xdc+\x92\xf0\xeb\xa0'

In [17]: md5.hexdigest()
Out[17]: '187ef4436122d1cc2f40dc2b92f0eba0'

In [18]: md5.update('cde'.encode('utf-8'))

In [19]: md5.hexdigest()
Out[19]: 'ab56b4d92b40713acc5af89985d4b786'

In [20]: md5.name
Out[20]: 'md5'

In [21]: md5.block_size, md5.digest_size
Out[21]: (64, 16)
```



```python
In [48]: hashlib.new('md5')
Out[48]: <md5 HASH object @ 0x00000216C3E67490>

In [49]: hashlib.new('sha1')
Out[49]: <sha1 HASH object @ 0x00000216C404C930>

In [50]: hashlib.new('sha256')
Out[50]: <sha256 HASH object @ 0x00000216C404C690>

In [51]: hashlib.new('sha512')
Out[51]: <sha512 HASH object @ 0x00000216C3E67DF0>
```



##### 密文登录

```python

# -*- coding: utf-8 -*-
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

import hashlib

def login(user, password):
    global db
    return db[user] == hashlib.md5(password.encode('utf-8')).hexdigest()

# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```

##### 密文+加盐 登录

```python
# 密文+加盐 登录
# -*- coding: utf-8 -*-
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
```



