#### WHERE 和 HAVING
> 别名是在内存中生成的，where 条件查询，只能用于从硬盘中，往内存中传输数据的过程中进行条件查询，符合条件的存入内存，不符合条件的不读取。相比较而言，having 是可以针对硬盘以及内存进行条件查询的。因此，如果对于聚合函数、别名等的条件查询，需要用having，而不是where。

#### 删除：truncate与delete
> - 使用```truncate students```进行删除可以连通id号一起删除，truncate 将表所有记录都删除了，所有结构的记录都删除，不可以roll back，可以触发触发器。
> - delete 只是删除了这一行记录，一行一行删，有记录，可以回滚roll back，被删除的id的数据虽然被删除了但还是占用着id号。

#### 用户自定义变量
```sql
SELECT @min_price:=MIN(price),@max_price:=MAX(price)
FROM shop;

SELECT * 
FROM shop 
WHERE price=@min_price OR price=@max_price;
```

#### 修改自增值 
```sql
ALTER TABLE tbl AUTO_INCREMENT = 100;
```

#### 批处理脚本

```shell
shell> mysql <batch-file
```

远程：
```shell
shell> mysql -h host -u user -p < batch-file
Enter password: ********
```
输出控制：
```shell
shell> mysql < batch-file | more
```
输出到文件：
```shell
shell> mysql < batch-file > mysql.out
```
获取交互式输出：
```shell
mysql -t
```
输出执行的语句：
```shell
mysql -v
```
`mysql`提示符使用脚本：
```sql
mysql> source filename;
mysql> \. filename
```

#### 窗口函数
```sql
WITH s1 AS (
   SELECT article, dealer, price,
          RANK() OVER (PARTITION BY article
                           ORDER BY price DESC
                      ) AS `Rank`
     FROM shop
)
SELECT article, dealer, price
  FROM s1
  WHERE `Rank` = 1
ORDER BY article;
```

#### 修改密码
```shell
mysqladmin -u root -p password new_password
```

#### AUTO_INCREMENT

> 为新纪录生成唯一标识

```sql
CREATE TABLE animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) NOT NULL,
     PRIMARY KEY (id)
);

# 自动分配序列号
INSERT INTO animals(name) VALUES
    ('dog'),('cat'),('penguin'),
    ('lax'),('whale'),('ostrich');
    
# 显示分配0来显示序列号
INSERT INTO animals(id, name) VALUES(0, 'groundhog');

# 若列为`NOT NULL`,也可以分配`NULL`生成序列号
INSERT INTO animals(id, name) VALUES(NULL, 'squirrel')

# 插入其他值时，序列会从该值继续递增
INSERT INTO animals(id, name) VALUES(100, 'rabbit')

# 重置默认值
ALTER TABLE tb1 AUTO_INREMENT = 100;

# 多列索引第二列指定AUTO_INCREMENT，生成的值为MAX(auto_increment_column) + 1 WHERE prefix=given-prefix
CREATE TABLE animals (
    grp ENUM('fish','mammal','bird') NOT NULL,
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name CHAR(30) NOT NULL,
    PRIMARY KEY (grp,id)
) ENGINE=MyISAM;

INSERT INTO animals (grp,name) VALUES
    ('mammal','dog'),('mammal','cat'),
    ('bird','penguin'),('fish','lax'),('mammal','whale'),
    ('bird','ostrich');

SELECT * FROM animals ORDER BY grp,id;

+--------+----+---------+
| grp    | id | name    |
+--------+----+---------+
| fish   |  1 | lax     |
| mammal |  1 | dog     |
| mammal |  2 | cat     |
| mammal |  3 | whale   |
| bird   |  1 | penguin |
| bird   |  2 | ostrich |
+--------+----+---------+
```

#### collate 核对
- `collate utf8_bin` 以二进制比较，区分大小写
- `collate utf8_general_ci` 一般比较，不区分大小写

#### InnoDB 表存储引擎