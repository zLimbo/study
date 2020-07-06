> MySQL函数用来实现数据库操作的一些高级功能, 这些函数大致分为以下几类: ==字符串函数、数学函数、日期时间函数、搜索函数、加密函数、信息函数==。

##### BIT_COUNT(BIT_OR(1<<day))

计算访问的天数。
`BIT_COUNT`统计二进制1的个数，`BIT_OR`或运算

##### TIMESTAMPDIFF(==YEAR==, birth, CURDATE())

计算当前年龄

##### LAST_INSERT_ID()

插入id

##### REGEXP_LIKE(str, reg)

正则匹配