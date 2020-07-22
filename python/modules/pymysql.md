#### 安装

```bash
pip install PyMySQL
```
若使用  `sha256_password` 或 `caching_sha_password`,则需要安装额外的依赖包
```bash
pip install PyMySQL[rsa]
```


#### pymysql.connections.Connection

##### 建立数据库连接
```python
__init__(host=None, user=None, password='', database=None, port=3306)
```
```python
import pymysql

conn = pymysql.connect('localhost', 'test', 'test', 'test')
```