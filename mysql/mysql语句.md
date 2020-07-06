#### 用户命令

##### 查看用户
```sql
use mysql
select * from user;
```

##### 创建用户
本地登录用户：
```sql
CREATE USER 'test_user'@'localhost' IDENTIFIED BY 'test_pwd';
```
远程登录用户:
```sql
CREATE USER 'test_user'@'%' IDENTIFIED BY 'test_pwd';
```

##### 删除用户
```sql
DROP USER 'test_user';
```
或
```sql
use mysql
DELETE FROM USER WHERE USER='test_user';
```

##### 授权用户
```sql
GRANT privileges ON database_name.table_name TO 'user_name'@'host' [WITH GRANT OPTION];
e.g.
GRANT ALL ON *.* TO 'test_user'@'%' WITH GRANT OPTION;
GRANT select, insert ON test_db.test_table TO 'test_user'@'%';
```

##### 撤销授权用户 
```sql
REVOKE privilege ON database_name.table_name FROM 'user_name'@'host';
```

##### 修改密码
```sql
SET PASSWORD FOR 'user_name'@'host' = 'new_password';
```
设置当前用户密码
```sql
SET PASSWORD = 'new_password';
```

#### 数据库操作

##### 创建数据库
```sql
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
    [create_option] ...

create_option: {
    [DEFAULT] CHARACTER SET [=] charset_name
  | [DEFAULT] COLLATE [=] collation_name
  | [DEFAULT] ENCRYPTION [=] {'Y' | 'N'}
}
```

##### 删除数据库
```sql
DROP DATABASE database_name;
```

##### 导入数据
```sql
LOAD DATA LOCAL INFILE path INTO TABLE table_name [(col1, col2, ...)]
[ FIELDS TERMINATED BY ','] # 分隔符
[ LINES TERMINATED BY '\r\n' ] # 行尾标记，windows系统
```
##### 导出数据
导出csv数据
```sql
SELECT a,b,a+b INTO OUTFILE '/tmp/result.txt'
  FROM test_table
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'；
```

#### 表操作
##### 建表

##### 添加列
```sql
ALTER TABLE table_name
ADD column_name attribute
[AFTER insert_position];
```
##### 修改列
```sql
ALTER TABLE table_name
CHANGE column_name new_column_name attribute;
```

##### 删除列
```sql
ALTER TABLE table_name
DROP column_name;
```

##### 重命名表
```sql
ALTER TABLE table_name
RENAME new_table_name;
```
##### 删除整张表
```sql
DROP TABLE table_name;
```

#### 表数据操作
##### 查找数据

```sql
SELECT
    [ALL | DISTINCT | DISTINCTROW ]
    [HIGH_PRIORITY]
    [STRAIGHT_JOIN]
    [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
    [SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    select_expr [, select_expr] ...
    [into_option]
    [FROM table_references
      [PARTITION partition_list]]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}, ... [WITH ROLLUP]]
    [HAVING where_condition]
    [WINDOW window_name AS (window_spec)
        [, window_name AS (window_spec)] ...]
    [ORDER BY {col_name | expr | position}
      [ASC | DESC], ... [WITH ROLLUP]]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [into_option]
    [FOR {UPDATE | SHARE}
        [OF tbl_name [, tbl_name] ...]
        [NOWAIT | SKIP LOCKED]
      | LOCK IN SHARE MODE]
    [into_option]

into_option: {
    INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        export_options
  | INTO DUMPFILE 'file_name'
  | INTO var_name [, var_name] ...
}
```
例子：
```mysql
SELECT 1 + 1 [ FROM DUAL ];

SELECT t1.*, t2.* 
FROM t1 INNER JOIN t2 ...

SELECT AVG(score), t1.* 
FROM t1 ...

SELECT CONCAT(last_name, ', ', first_name) [AS] full_name 
FROM mytable 
ORDER BY full_name;

SELECT t1.name, t2.salary 
FROM employee AS t1, info AS t2 
WHERE t1.name = t2.name;

SELECT college, region AS r, seed AS s
FROM tournament
ORDER BY region, seed;
(ORDER BY r, s)
(ORDER BY 2, 3)

SELECT a, b, COUNT(c) AS t
FROM test_table
GROUP BY a, b
ORDER BY a, t DESC;

SELECT COUNT(col1) AS col2
FROM t
GROUP BY col2
HAVING col2 = 2;

SELECT user, MAX(SALARY)
FROM users
GROUP BY user
HAVING MAX(salary) > 10;

SELECT *
FROM tbl
LIMIT 5, 10; # Retrieve rows 6-15
(LIMIT 10 OFFSET 5)

SELECT name, birth, death, TIMESTAMPDIFF(YEAR, birth, death) AS age 
FROM pet 
WHERE death IS NOT NULL 
ORDER BY age;

SELECT name, birth 
FROM pet 
WHERE MONTH(birth) = 5;
( HAVING MONTH(birth) )

SELECT name, birth 
FROM pet 
WHERE MONTH(birth) = MONTH(DATE_ADD(CURDATE(), INTERVAL 2 MONTH));
( WHERE MONTH(birth) = MOD(MONTH(CURDATE()) + 1, 12) + 1) )

SELECT 0 IS NULL, 1 IS NOT NULL, '' IS NOT NULL, NULL IS NULL, NULL = NULL, NULL <> NULL, 0 = NULL, 1 <> NULL;
+-----------+---------------+----------------+--------------+-------------+--------------+----------+-----------+
| 0 IS NULL | 1 IS NOT NULL | '' IS NOT NULL | NULL IS NULL | NULL = NULL | NULL <> NULL | 0 = NULL | 1 <> NULL |
+-----------+---------------+----------------+--------------+-------------+--------------+----------+-----------+
|         0 |             1 |              1 |            1 |        NULL |         NULL |     NULL |      NULL |
+-----------+---------------+----------------+--------------+-------------+--------------+----------+-----------+

SELECT * 
FROM pet 
WHERE name LIKE 'b%';

SELECT * 
FROM pet 
WHERE name NOT LIKE '_____';

SELECT * 
FROM pet 
WHERE REGEXP_LIKE(name, '^.{4,5}$') 
ORDER BY LENGTH(name);

SELECT * 
FROM pet 
WHERE REGEXP_LIKE(name, BINARY 'b');
(WHERE REGEXP_LIKE(name, 'b', 'c');

SELECT pet.name, TIMESTAMPDIFF(YEAR, birth, date) AS age, remark 
FROM pet INNER JOIN event 
ON pet.name = event.name 
WHERE event.type = 'litter';

SELECT p1.name, p1.sex, p2.name, p2.sex, p1.species
FROM pet AS p1 INNER JOIN pet AS p2
ON p1.species = p2.species
AND p1.sex = 'f' AND p1.death IS NULL
AND p2.sex = 'm' AND p2.death IS NULL;

SELECT * 
FROM pet LEFT INNER JOIN event
ON pet.name = event.name;

SELECT article, MAX(price) AS price
FROM   shop
GROUP BY article
ORDER BY article;

#子查询
SELECT article, dealer, price
FROM   shop
WHERE  price=(SELECT MAX(price) FROM shop);

# or 
SELECT s1.article, s1.dealer, s1.price
FROM shop s1
LEFT JOIN shop s2 ON s1.price < s2.price
WHERE s2.article IS NULL;

# or
SELECT article, dealer, price
FROM shop
ORDER BY price DESC
LIMIT 1;

# 低效的关联子查询
SELECT article, dealer, price
FROM shop s1
WHERE price = ( 
    SELECT MAX(price)
    FROM shop s2
    WHERE s1.article = s2.article)
   
# or 连接+无关联子查询
SELECT s1.article, s1.dealer, s1.price
FROM shop s1
JOIN (
    SELECT article, MAX(price)
    FROM shop
    GROUP BY article ) AS s2
ON s1.article = s2.article AND s1.price = s2.price;

# or 左连接
SELECT s1.article, s1.dealer, s1.price
FROM shop s1 LEFT JOIN shop s2
ON s1.article = s2.article AND s1.price < s2.price
WHERE s2.price IS NULL
ORDER BY s1.article;

# UNION
SELECT field1_index, field2_index
    FROM test_table 
    WHERE field1_index = '1'
UNION
SELECT field1_index, field2_index
    FROM test_table 
    WHERE field2_index = '1';
    
# 访问的天数（而非次数）
SELECT year,month,BIT_COUNT(BIT_OR(1<<day)) AS days 
FROM t1
GROUP BY year,month;
```

##### 更新表中数据
```sql
UPDATE table_name
SET column_name=new_value
WHERE condition;
```
##### 删除表中数据
```sql
DELETE FROM table_name
WHERE condition;
```