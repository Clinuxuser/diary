git操作
-------

安装git
~~~~~~~

::

   yum -y install git

   git config --global user.name "dongzl"
   git config --global user.email "<dongzl@wangtai-tech.com>"
   git config --global push.default simple


   ssh-keygen -t rsa -C '<dongzhenling@wangtai-tech.com>'
   cd
   cd .ssh
   cat id_rsa.pub
   网页上生成秘钥即可

git 命令
~~~~~~~~

::

   git clone git@192.168.10.10:ana/src/col/col/collection.git

   git status
   git add -A 将本地修改的文件推到本地缓存区
   git commit 写说明
   git commit --amend  重新修改描述
   git push

   回退版本：
   git status
   git log

   git  reset  --hard  重置
   git checkout -b release-1.0.0 origin/release-1.0.0 切换分支 为release-1.0.0分支 从origin/release-1.0.0
   git branch -D master 删除本地master分支

   回退版本:gir reset --hard  版本号
   git reset --hard 9e93c73e770cd30bc47a402cab350f323215e3fe

   删除本地分支：git branch -d  分支名称
       如：git branch -d dzl-rule
   删除远程分支：git push origin -d 分支名称
       如：git push origin -d dzl-rule

拉取tag
~~~~~~~

::

   git fetch --tags

这个命令会从远程仓库获取所有标签的最新信息，并将它们存储在本地。之后，你可以使用git
checkout命令切换到特定的标签。
如果你只想拉取特定的标签，可以使用以下命令：

::

   git fetch --tags <repository> <tag>

其中，是远程仓库的名称或URL，是你要拉取的标签名称。

拉取完成后，你可以使用git checkout命令切换到所需的标签。例如：

::

   git checkout <tag>

git使用问题
~~~~~~~~~~~

问题1：22端口被禁用
^^^^^^^^^^^^^^^^^^^

问题现象
''''''''

::

   $ git pull
       ssh: connect to host github.com port 22: Connection refused
       fatal: Could not read from remote repository.

       Please make sure you have the correct access rights
       and the repository exists.

问题原因
''''''''

::

   ssh: connect to host github.com port 22: Connection refused这个错误提示的是连接github.com的22端口被拒绝了

解决思路
''''''''

给~/.ssh/config文件里添加如下内容，这样ssh连接GitHub的时候就会使用443端口。

::

   Host github.com
     Hostname ssh.github.com
       Port 443

解决方案
''''''''

使用GitHub的443端口 1.vim ~/.ssh/config

2.添加以下内容

::

   # Add section below to it
   Host github.com
       Hostname ssh.github.com
       Port 443

3.执行命令 sh -T git@github.com
