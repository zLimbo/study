> - 此模块提供了将二进制数据编码为可打印的 ASCII 字符以及将这些编码解码回二进制数据的函数。
> - 此模块提供了两个接口。新的接口提供了从 类字节对象 到 ASCII 字节 bytes 的编码，以及将 ASCII 的 类字节对象 或字符串解码到 bytes 的操作。

| 接口                            | 说明 |
| :------------------------------ | :--- |
| **b64encode(s, altchars=None)** |      |
| **b64decode(s, altchars=None)** |      |
| standard_b64encode(s)           |      |
| standard_b64decode(s)           |      |
| **urlsafe_b64encode(s)**        |      |
| **urlsafe_b64decode(s)**        |      |
| b32encode(s)                    |      |
| b32decode(s)                    |      |
| b16encode(s)                    |      |
| b16decode(s)                    |      |
| a85encode(s)                    |      |
| a85decode(s)                    |      |
| b85encode(s)                    |      |
| b85decode(s)                    |      |