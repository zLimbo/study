#### `sort`

> 它将文件的每一行作为一个单位排序，从首字母开始，依次按照`ASCII`码值比较，最后升序输出

##### 语法

```shell
sort [Option] file [-o newFile]
```

```shell
Option:
	-r 降序排列（默认升序）
	-u 去除重复行
	-o 输出到新文件
	-ts s为分隔符
	-kn 第n列作为排序关键字
	-b 忽略前导空格
	-R 随机排序
```

##### 例子

```shell
sort -n -t: -k3 passwd
sort -nr -t: -k3 passwd -o new.txt
sort -u passwd
sort -R passwd
```



#### 参考：

[Shell编程之文本处理工具与bash的特性](https://mp.weixin.qq.com/s/7pfE3S-uDSLOG1AZSj3D1A)

