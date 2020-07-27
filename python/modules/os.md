#### os
| 方法                                     | 说明                                                         |
| :--------------------------------------- | :----------------------------------------------------------- |
| getcwd()                                 | 当前目录                                                     |
| chdir(path)                              | 切换目录                                                     |
| listdir(path=None)                       | 路径下的目录或文件                                           |
| mkdir(path, mode=511)                    | 创建文件夹                                                   |
| makedirs(name, mode=511, exist_ok=False) | 递归创建文件夹                                               |
| walk(top)                                | 从top开始遍历，返回生成器，为(当前目录名，目录下所有目录，目录下所有文件) |
| remove(path)                             | 删除文件                                                     |
| rmdir(path)                              | 删除目录                                                     |
| removedirs(name)                         | 递归删除文件和空文件夹                                       |
| rename(old, new)                         | 重命名                                                       |
| write(fd, data)                          | 写入bytes对象到一个文件                                      |
| scandir(path=None)                       | 返回DirEntry的迭代器                                         |
| getenv(key)                              | 读取环境变量                                                 |
| stat(path)                               | 路径信息                                                     |
| truncate(path, length)                   | 截断一个文件，固定长度                                       |
| putenv(key, value)                       | 设置环境变量                                                 |
| system()                                 | 运行shell命令                                                |
| access(path, mode)                       | 路径拥有的权限，如os.R_OK, os.W_OK                           |
| chmod(path, mode)                        | 改变路径权限                                                 |
| cpu_count()                              | cpu核心                                                      |
| getlogin()                               | 当前登录用户名                                               |
| getpid()                                 | 当前进程id                                                   |
| getppid()                                | 当前父进程id                                                 |
| waitpid(pid, options)                    | 等待某个进程结束（Windows忽略options）                       |
| kill(pid, signal)                        | 杀进程                                                       |
| name                                     | 'posix'(Linux, Unix or Mac OS X) or 'nt'(Windows)            |
| uname                                    | 详细系统信息（Windows不提供）                                |
| environ                                  | 所有环境变量                                                 |


#### os.path

| 方法                        | 说明                                       |
| :-------------------------- | :----------------------------------------- |
| abspath(path)               | 返回绝对路径                               |
| basename(path)              | 返回文件名                                 |
| commonprefix(list)          | 返回多个路径的公共最长路径                 |
| dirname(path)               | 返回文件路径                               |
| exists(path)                | 判定路径存在与否                           |
| expanduser(path)            | 将`~`和`~user`转换为用户目录               |
| getatime(path)              | 最近访问时间(浮点型秒数)                   |
| getmtime(path)              | 最近修改时间                               |
| getctime(path)              | 创建时间                                   |
| getsize(path)               | 文件大小                                   |
| isabs(path)                 | 判断是否为绝对路径                         |
| isfile(path)                | 判断是否为文件                             |
| isdir(path)                 | 判断是否为目录                             |
| join(path1[, path2[, ...]]) | 合并目录                                   |
| realpath(path)              | 返回真实路径                               |
| relpath(path[, start])      | 计算相对路径                               |
| samefile(path1, path2)      | 判断目录或文件是否相同                     |
| sameopenfile(fp1, fp2)      | fp1和fp2是否指向同一文件                   |
| split(path)                 | 把路径分割成dirname和basename,返回一个元组 |
| splitdrive(path)            | 返回驱动器名称和路径组成的元组             |
| splitext(path)              | 返回路径名和文件扩展名组成的元组           |