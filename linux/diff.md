#### `diff`

> 逐行比较文件的不同，其方式是告诉我们怎样改变第一个文件之后与第二个文件相同

##### 语法

```shell
diff [Option] file1 file2
```

```shell
Option:
	-b 不检查空格
	-B 不检查空白行
	-i 不检查大小写
	-w 忽略所有的空格
	--normal 正常格式显示（默认）
	-c 上下文格式显示
	-u 合并格式显示
```



```shell
#cat file1
```

