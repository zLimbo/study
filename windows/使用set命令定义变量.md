使用`set`命令定义变量
```shell
set PrjPath=C:\Users\Administrator\Desktop\PrjPath
```
使用 `%%` 2个百分号引用变量
```shell
echo %PrjPath%
```
下面在环境变量`PATH`后面添加路径
```shell
set PATH=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\IDE

echo %PATH%
```