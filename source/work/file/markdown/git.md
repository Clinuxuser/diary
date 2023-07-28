## git操作

### 安装git
```
yum -y install git

git config --global user.name "dongzl"
git config --global user.email "<dongzl@wangtai-tech.com>"
git config --global push.default simple


ssh-keygen -t rsa -C '<dongzhenling@wangtai-tech.com>'
cd
cd .ssh
cat id_rsa.pub
网页上生成秘钥即可
```

### git 命令
```
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
```

### 拉取tag
```
git fetch --tags
```
这个命令会从远程仓库获取所有标签的最新信息，并将它们存储在本地。之后，你可以使用git checkout命令切换到特定的标签。
如果你只想拉取特定的标签，可以使用以下命令：
```
git fetch --tags <repository> <tag>
```
其中，<repository>是远程仓库的名称或URL，<tag>是你要拉取的标签名称。

拉取完成后，你可以使用git checkout命令切换到所需的标签。例如：
```
git checkout <tag>
```