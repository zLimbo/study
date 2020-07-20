#### `cut ` 

> 列截取工具

##### 语法

```shell
cut [Option] file
```

```shell
Option:
	-ca[-[b]] 以字符为单位进行分割截取
	-d[separator] 自定义分隔符，默认为制表符\t
	-fn1[,n2,...] 与-d一起使用，指定截取那个区域
```

##### 例子

```shell
cut -d: -f1 passwd
cut -d: -f1,3,5 passwd
cut -c6 passwd
cut -c2-5 passwd
cut -c3- passwd
```

