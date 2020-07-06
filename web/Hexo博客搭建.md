---
title: Hexo博客搭建
date: 2020-06-04 16:31:15
categories: 
- web前端
tags:
- Hexo
- Nginx
- Node.js
description: 记述下博客搭建的过程和遇到的问题
toc: true

---

# 搭建过程

## 安装相关软件

### Git

git安装：

- Windows：下载并安装 [git](https://git-scm.com/download/win).

- Mac：使用 [Homebrew](http://mxcl.github.com/homebrew/), [MacPorts](http://www.macports.org/) 或者下载 [安装程序](http://sourceforge.net/projects/git-osx-installer/)。

- Linux (Ubuntu, Debian)：`sudo apt-get install git-core`

- Linux (Fedora, Red Hat, CentOS)：`sudo yum install git-core`

git安装后，在本地配置用户信息：

`git config --global user.name "github用户名"`

`git config --global user.email "github注册邮箱"`

### Node.js

> **版本不低于8.10,建议10.0以上**

[菜鸟教程](https://www.runoob.com/nodejs/nodejs-tutorial.html)对[Node.js](http://nodejs.cn/)的相关介绍：

> Node.js 是运行在服务端的 JavaScript。
>
> Node.js 是一个基于Chrome JavaScript 运行时建立的一个平台。
>
> Node.js是一个事件驱动I/O服务端JavaScript环境，基于Google的V8引擎，V8引擎执行Javascript的速度非常快，性能非常好。

这里使用NVM安装，NVM(Node Version Manager)是Node.js的版本管理软件，可在不同版本间切换。

windows安装nvm通过下载[nvm-windows](https://github.com/coreybutler/nvm-windows/releases)安装，下面是Linux上的安装过程。

1. 下载并安装NVM脚本：

   `curl https://raw.githubusercontent.com/creationix/nvm/v0.13.1/install.sh | bash`

2. 更新环境配置： `source ~/.bash_profile`

3. 查看远程仓库的版本：`nvm list-remote` 

4. 安装相应版本：`nvm install v12.17.0` 

5. 查看本地仓库的版本：`nvm list`

6. 切换版本：`nvm use v12.17.0`

7. 设置默认版本：`nvm alias default v12.17.0`

### Hexo

使用npm安装 ：`sudo npm install -g hexo-cli`

## 搭建博客

1. 初始化博客：`hexo init mysite` 
2. 新建一篇文章:  `hexo n "hello world"` 或  `hexo new "hello world"`
3. 清除缓存：`hexo clean` 
   * 网页正常可忽略
4. 生成相关网页数据：`hexo g` 或 `hexo generate`
5. 启动服务器预览： `hexo s` 或 `hexo server` 
   * 默认地址在 `localhost:4000`，浏览器输入即可预览
   * `hexo s -p 8000` 更换端口，`hexo s -i 192.168.1.1` 自定义IP

6. 部署博客：`hexo d` 或 `hexo deploy` 
   * 生成部署合并命令：`hexo g -d`
   * 此步先设置好相关远程服务器git库再进行

## 网站部署

**博客可以推送到github服务器上，也可以推送到自己的云服务器上。**

在本地生成ssh密钥：

`ssh-keygen -t rsa -C "github注册邮箱"`

然后三个回车，默认无密码

### 部署在github上

将`.ssh`文件夹下`id_rsa.pub`公钥添加到github的`SSH keys`中（在settings中)。

github创建一个`repository`仓库，命名为 `zLimbo.github.io`（zLimbo改为自己的github用户名)。

编辑`mysite`文件夹下的`_config.yml`文件，文件最后如下配置：

```yaml
deploy:
  type: git
  repo: git@github.com:zLimbo/zLimbo.github.io.git
  branch: master
```

然后可进行博客部署`hexo d`，访问`zLimbo.github.io`即可浏览博客。

### 部署在云服务器上

对于云服务器，将`id_rsa.pub`公钥添加到服务器`.ssh`文件夹下的`authorized_keys`文件中。

云服务器使用`git`初始化一个裸仓库：`git init --bare mysite.git`

创建一个存放网站数据的文件夹：`mkdir -p /data/www/mysite`

在`mysite.git/hooks`下创建`post-receive`脚本文件，加入：

```bash
#!/bin/bash
git --work-tree=/data/www/mysite --git-dir=/root/git/mysite.git checkout -f
# 不同的文件路径需修改
```

保存后，添加可执行权限：`chmod +x mysite.git/hooks/post-receive`

这样，在网站部署推送至远程服务器仓库时，该钩子脚本会将最新的`master`数据复制到工作目录下。

**接下来通过[nginx](https://www.nginx.cn/doc/general/overview.html)部署web服务，配置静态资源访问目录到自定义目录**

安装`nginx`：`yum install -y nginx`

打开配置文件`/etc/nginx/nginx.conf`，查找并修改如下配置：

```bash
server {
        listen       80 default_server;	# 服务器需开放80口，或者使用其他开放端口
        listen       [::]:80 default_server;
        server_name  zlimbo.com;	# 没有域名暂不修改
        root         /data/www/mysite;
```

然后可进行博客部署`hexo d`，访问服务器IP即可浏览博客。

## 主题

pass

# 遇到的问题

pass



# 参考文档

[1] [Hexo中文文档](https://hexo.io/zh-cn/docs/)

[2] [GitHub+Hexo 搭建个人网站详细教程](https://zhuanlan.zhihu.com/p/26625249)

[3] [在CentOS 7上安装Node.js的4种方法](https://blog.csdn.net/xuaa/article/details/52262586)

[4] [如何在个人服务器上部署Hexo博客](https://www.jianshu.com/p/196773379a78)

[5] [Hexo 个人博客部署到 CentOS 个人服务器](https://segmentfault.com/a/1190000010680022)