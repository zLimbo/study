#### 客户端

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



#### 服务端

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

