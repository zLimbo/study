#### TCP客户端

```python
import socket

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接IP和端口
s.connect(('wwww.sina.com.cn', 80))
# 发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 数据为HTTP头和网页本身
header, html = data.split('\r\n', 1)
```



#### TCP服务端

```python
# 服务端：
import socket
import threading
import time

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定监听ip和端口
s.bind(('127.0.0.1', 8081))
# 监听
s.listen(5)
print('Waiting for connection...')
# 使用进程处理不同的请求
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
```

```python
# 客户端
import socket
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8081))
print(s.recv(1024).decode('utf-8'))
for data in [str(random.random()).encode('utf-8') for _ in range(20)]:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
```



#### UDP

> TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据。相对TCP，UDP则是面向无连接的协议。
>
> 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
>
> 虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。

```python
# 服务端

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))

print('Bind UDP on 9999')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
```

```python
# 客户端
import socket

s = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.sendto(data, ('127.0.0.1', 8888))
    print(s.recv(1024).decode('utf-8'))
s.close()
```

```ascii
┌────────────────────────────────────────────────────────┐
│Command Prompt                                    - □ x │
├────────────────────────────────────────────────────────┤
│$ python udp_server.py                                  │
│Bind UDP on 9999...                                     │
│Received from 127.0.0.1:63823...                        │
│Received from 127.0.0.1:63823...                        │
│Received from 127.0.0.1:63823...                        │
│       ┌────────────────────────────────────────────────┴───────┐
│       │Command Prompt                                    - □ x │
│       ├────────────────────────────────────────────────────────┤
│       │$ python udp_client.py                                  │
│       │Welcome!                                                │
│       │Hello, Michael!                                         │
└───────┤Hello, Tracy!                                           │
        │Hello, Sarah!                                           │
        │$                                                       │
        │                                                        │
        │                                                        │
        └────────────────────────────────────────────────────────┘
```

> UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的9999端口与TCP的9999端口可以各自绑定。