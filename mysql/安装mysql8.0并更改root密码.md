#### CentOS7 安装 MySQL

添加mysql yum源
```bash
rpm -Uvh https://repo.mysql.com//mysql80-community-release-e17-2.noarch.rpm
```
yum查看
```bash
yum repolist all | grep mysql
```
安装
```bash
yum install mysql-community-server
```
启动服务
```bash
service mysqld start
```
查看状态
```bash
service mysqld status
```
查看临时密码
```bash
grep 'temporary password' /var/log/mysqld.log
```
登录
```bash
mysql -uroot -pxxxxxx
```

#### 更改root密码

设置两个全局参数
> 这样才可以自定义密码格式和长度，否则就必须按照配置文件默认设置的密码长度和密码格式。

```sql
set global validate_password.policy=0;
set global validate_password.length=1;
```
更改root密码
```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
```
root远程登录配置
```sql
CREATE USER 'root'@'%' IDENTIFIED BY 'password';
GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION;
```
> `WITH GRANT OPTION` 这个选项表示该用户可以将自己拥有的权限授权给别人。

> 如发现提示`caching_sha2_password`无法加载，或者`caching_sha2_password`模块找不到，是因为`caching_sha2_password`是默认的身份验证插件而不是之前版本的`mysql_native_password`，此时需要设置账户的身份验证方：
```sql
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
```