一. 常用编译命令选项
假设源程序文件名为`test.c`。

1. 无选项编译链接：
    ```shell
    gcc test.c
    ```
    作用：将test.c预处理、汇编、编译并链接形成可执行文件。这里未指定输出文件，默认输出为`a.out`。编译成功后可以看到生成了一个`a.out`的文件。在命令行输入`./a.out` 执行程序。`./`表示在当前目录，`a.out`为可执行程序文件名。

2. 选项 `-o`:
    ```shell
    gcc test.c -o test
    ```
    作用：将test.c预处理、汇编、编译并链接形成可执行文件`test`。`-o`选项用来指定输出文件的文件名。输入`./test`执行程序。

3. 选项 `-E`;
    ```shell
    gcc -E test.c -o test.i
    ```
    作用：将`test.c`预处理输出`test.i`文件。

4. 选项 `-S`:
    ```shell
    gcc -S test.i
    ```
    作用：将预处理输出文件`test.i`汇编成`test.s`文件。

5. 选项 `-c`:
    ```shell
    gcc -c test.s
    ```
    作用：将汇编输出文件`test.s`编译输出`test.o`文件。

6. 无选项链接:
    ```shell
    gcc test.o -o test
    ```
    作用：将编译输出文件`test.o`链接成最终可执行文件`test`。输入`./test`执行程序。

7. 选项-O
用法：`gcc -O1 test.c -o test`
作用：使用编译优化级别1编译程序。级别为1~3，级别越大优化效果越好，但编译时间越长。输入./test执行程序。

二. 多源文件的编译方法

如果有多个源文件，基本上有两种编译方法：
[假设有两个源文件为`test.c`和`testfun.c`]

1. 多个文件一起编译。
    ```shell
    gcc testfun.c test.c -o test
    ```
    作用：将`testfun.c`和`test.c`分别编译后链接成`test`可执行文件。

2. 分别编译各个源文件，之后对编译后输出的目标文件链接:
    ```shell
    # 将testfun.c编译成testfun.o
    gcc -c testfun.c 
    
    # 将test.c编译成test.o
    gcc -c test.c 
    
    # 将testfun.o和test.o链接成test
    gcc -o testfun.o test.o -o test 
    ```
    以上两种方法相比较，第一中方法编译时需要所有文件重新编译，而第二种方法可以只重新编译修改的文件，未修改的文件不用重新编译。