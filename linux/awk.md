#### `awk`

> - awk是一种处理文本文件的语言，是一个强大的文本分析工具。
>- awk把文件逐行读入，（空格，制表符）为默认分割符将每行切片，切开的部分再进行各种分析处理。

##### 语法

```bash
awk [-F field-separator] 'commands' input-file(s)
```

`field-separator`为分隔符，默认为空格和制表符

##### 内建变量

- `FILENAME` 浏览的文件名
- `FS(Field Separator)` 输入字段分隔符
- `OFS(Output Field Seperator)` 输出字段分隔符，在语法里用`,`号表示
- `RS(Record Separator)` 记录分隔符
- `ORS(Ouput Record Separator)` 输出记录分隔符
- `NF(Number of Field)` 浏览记录的字段个数
- `NR(Number of Record)` 已读的记录数

##### 函数

- `toupper(s)` 返回大写
- `tolower(s)` 返回小写
- `length(s)` 返回长度
- `substr(s, p)` 返回字符串从`p`开始的后缀

##### 条件操作

- `<` `<=` `>` `>=` `==` `!=`
- `$$` `||` `!`

##### 正则匹配

- `~` 匹配正则

- `!~` 不匹配正则

##### 流程控制

- `if ... else ...` 
- `while ... do ...`
-  `for` `break` `continue` 

#### 使用

1. 只显示`/etc/passwd`的账户：

   ```bash
   awk -F : '{print $1}' /etc/passwd
   ```

2. 显示`/etc/passwd`的第一列和第七列

   ```bash
   awk 'BEGIN {{FS=":"} {print FS "\tstart1,start7"}} {print $1 "," $7} END {print "end1,end7"}' /etc/passwd
   ```

   > BEGIN在文本处理前执行，END在所有文本处理后执行，不加这两个关键字 ，上述代码会在每一行都执行

3. 显示`/etc/passwd`每行行号、列数、字符长度、大写完整内容

   ```bash
   awk -F : '{ print NR "\t" NF "\t" length($0) "\t" toupper($0) }' /etc/passwd
   ```

4. 显示`/etc/passwd`行字符数大于30的行号和其字符数

   ```bash
   awk -F : 'length($0) < 50 { print NR "\t" length($0) }' /etc/passwd
   ```

5. 查找`/etc/passwd`中含有`a`字符的行

   ```bash
   awk -F : '$0 ~ /.*a.*/' /etc/passwd
   ```

6. 查找`/etc/passwd`中不含有`a`字符的行

   ```bash
    awk -F : '$0 !~ /.*a.*/' /etc/passwd
   ```

7. 查找`/etc/passwd`中以`sys`开头的用户的行

   ```bash
    awk -F : '{ if ($1 ~ /^sys/) { print $0 } else { print "-" } }' /etc/passwd
   ```

   可建立脚本文件`test.sh`:

   ```sh
   {
   	if ($1 ~ /^sys/) {
   		print $0
   	} else {
   		print "-"
   	}
   }
   ```

   然后执行：

   ```bash
   awk -F : -f test.sh /etc/passwd
   ```

8. 使用`for`循环和分隔符

   ```bash
    echo "1,2,3|4,5,6|7,8,9" | awk 'BEGIN {{FS=","} {RS="|"} {ORS="\t"}}{for(i = 1; i <= NF; ++i) {print $i}}'
   ```

   

