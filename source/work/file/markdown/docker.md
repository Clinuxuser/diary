# docker学习笔记
目录：
[TOC]



## docker说明
[前言 · Docker -- 从入门到实践](https://docker-practice.github.io/zh-cn/)

### 基本概念
#### 容器
操作系统分为 内核 和 用户空间。对于 Linux 而言，内核启动后，会挂载 root 文件系统为其提供用户空间支持。而 Docker 镜像（Image），就相当于是一个 root 文件系统。比如官方镜像 ubuntu:18.04 就包含了完整的一套 Ubuntu 18.04 最小系统的 root 文件系统。
Docker 镜像 是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像 不包含 任何动态数据，其内容在构建之后也不会被改变。

#### 镜像
镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的 类 和 实例 一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。

容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 命名空间。因此容器可以拥有自己的 root 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全。也因为这种隔离的特性，很多人初学 Docker 时常常会混淆容器和虚拟机。

前面讲过镜像使用的是分层存储，容器也是如此。每一个容器运行时，是以镜像为基础层，在其上创建一个当前容器的存储层，我们可以称这个为容器运行时读写而准备的存储层为 容器存储层。

容器存储层的生存周期和容器一样，容器消亡时，容器存储层也随之消亡。因此，任何保存于容器存储层的信息都会随容器删除而丢失。

按照 Docker 最佳实践的要求，容器不应该向其存储层内写入任何数据，容器存储层要保持无状态化。所有的文件写入操作，都应该使用 数据卷（Volume）、或者 绑定宿主目录，在这些位置的读写会跳过容器存储层，直接对宿主（或网络存储）发生读写，其性能和稳定性更高。

数据卷的生存周期独立于容器，容器消亡，数据卷不会消亡。因此，使用数据卷后，容器删除或者重新运行之后，数据却不会丢失。
#### 仓库
镜像构建完成后，可以很容易的在当前宿主机上运行，但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，Docker Registry 就是这样的服务。

一个 Docker Registry 中可以包含多个 仓库（Repository）；每个仓库可以包含多个 标签（Tag）；每个标签对应一个镜像。

通常，一个仓库会包含同一个软件不同版本的镜像，而标签就常用于对应该软件的各个版本。我们可以通过 <仓库名>:<标签> 的格式来指定具体是这个软件哪个版本的镜像。如果不给出标签，将以 latest 作为默认标签。

以 Ubuntu 镜像 为例，ubuntu 是仓库的名字，其内包含有不同的版本标签，如，16.04, 18.04。我们可以通过 ubuntu:16.04，或者 ubuntu:18.04 来具体指定所需哪个版本的镜像。如果忽略了标签，比如 ubuntu，那将视为 ubuntu:latest。

仓库名经常以 两段式路径 形式出现，比如 jwilder/nginx-proxy，前者往往意味着 Docker Registry 多用户环境下的用户名，后者则往往是对应的软件名。但这并非绝对，取决于所使用的具体 Docker Registry 的软件或服务。

## docker命令
### docker环境信息命令
```
docker info             //用于检测Docker是否正确安装
docker version          
```
### Docker运维操作
```
-- attcach
docker attach命令对应用开发者很有用，可以连接到正在部署的容器，观察容器的运行状况，或与容器的主进程进行交互。

-- inspect
docker inspect
用于查看镜像和容器的详细信息，默认会列出全部信息，可以通过--format 参数来指定输出的模板格式，以便输出特定格式。

--ps 
docker ps
docker ps 命令可以查看容器的CONTAINER ID ,NAME，IMAGE NAME，端口开启及绑定容器启动执行的COMMAND。最常用的功能是通过ps来找到CONTAINER ID ，以便对特定容器进行操作。
docker ps 默认显示当前正在运行中的container
docker ps -a 查看包括已经停止的所有容器
docker ps -l 显示最新启动的一个容器（包括已停止的）

-- images 
docker images ls
docker images 列出机器上镜像**
其中我们可以根据REPOSITORY来判断这个镜像是来自哪个服务器，
如果没有/ 则表示官方镜像，类似于username/repos_name 表示GitBub的个人公共库，类似于http://regsistory.example.com:5000/repos_name则表示的是私服。

-- search [name] 
docker search hello-world
在docker index中搜索image
搜索的范围是官方镜像和所有个人公共镜像。NAME列的 / 后面是仓库的名字。

-- pull 
docker pull chenlicn163/hello-word
从docker registry server 中下pull image 或 repository
docker pull redis
上面的命令需要，在docker v1.2版本之前，会下载官方镜像的centos仓库的所有镜像，而从v1.3开始。官方文档的说明变了，will pull the centos:latest image, its intermediate layers and any aliases of the same id，也就是只会下载tag为latest的镜像（以及同一images id 的其他tag）
明确指定具体的镜像
docker pull centos:centos
从某个的公共仓库拉取，形如 docker pull username/repositroy<:tag_name>
docker pull seanlook/centos:centos6
如果你没有网络，或者从其它私服获取镜像，形如docker pull http://registry.domain.com:5000/repos:
docker pull dl.dockerpool.com:5000/mongo:latest

-- push 
docker push hello-word
推送一个images或repository到registry（push）
docker push [images-name]
与上面的pull对应，可以推送到Docker Hub的Public、Private以及私服、但不能推送到Top Level Repository
docker push seanlook/mongo
docker push registry.tp-link.net:5000/mongo
在 repostiroy 不存在的情况下，命令行下push上去的会为我们创建私有库，然而通过浏览器创建的默认为公共库。

-- run 
docker run -d --hostname my-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3.73-management
从images 启动一个container
当利用docker run 来创建容器时，docker在后台运行的标准包括：
·检查本地是否存在指定镜像，不存在就从公有仓库下载。
·利用镜像创建并启动一个容器
·分配一个文件系统，并在只读的镜像层外面挂载一层可读写层。
·从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去。
·从地址池配置一个ip地址给容器
·执行完毕后容器被终止。

-- 使用image 创建container并执行相应命令，然后停止。
docker run ubuntu ehco 'hello world'
这是简单的方式，跟在本地直接执行 echo 'hello world' 几乎感觉不到任何区别，而实际上它会从本地ubuntu：latest镜像启动到一个容器，并执行打印命令退出（docker ps -l 可查看）.需要注意的是，默认有一个rm=true的参数，即完成操作后停止容器并从文件系统移除。因为docker的容器实在太轻量级了，很多时候用户都是随时删除和新创建容器。

容器启动后会自动随机生成一个Container ID，这个ID 在后面commit命令后可以变为IMAGE ID 。

-- 使用image创建container并进入交互模式，login shell 是/bin/bash
docker run -i-t --name myubuntu ubuntu /bin/bash
上面的--name参数可以指定启动后的容器名字，如果不指定则docker会帮我们取一个名字。镜像ubuntu可以用IMAGE ID (dba1062371c)代替，并且会启动一个伪终端，但通过ps或top命令我们却只能看到一两个进程。因为容器的核心是所执行的应用程序，所需要的资源都是应用程序运行所必须的，除此之外，并没有其它的资源，可见Docker对资源的利用率极高，此时使用exit或ctrl+d退出后，这个容器也就消失了 。

-- 运行出一个container放到后台运行
docker run -d hello-world
它将直接把启动的container挂起放在后台运行（这才叫saas），并且会输出一个CONTAINER ID，通过docker ps可以看到这个容器的信息，可在container外面查看它的输出docker logs ae60c4b64205，也可以通过docker attach ae60c4b64205连接到这个正在运行的终端，此时在Ctrl+C退出container就消失了，按ctrl-p ctrl-q可以退出到宿主机，而保持container仍然在运行
另外，如果-d启动但后面的命令执行完就结束了，如/bin/bash、echo test，则container做完该做的时候依然会终止。而且-d不能与--rm同时使用
可以通过这种方式来运行memcached、apache等。

-- 映射host到container的端口和目录
映射主机到容器的端口是很有的，比如在container中运行的nginx，端口为80，运行容器的host可以连接container的internal_ip：80访问，如果有其它主机访问Nginx需求那就可以通过-p选项，形如-p
存在以下几种写法：
-p 80:80 这个即是默认情况下，绑定主机所有网卡（0.0.0.0）的80端口到容器的80端口上。 -p 127.0.0.1:80:80 只绑定localhost这个接口的80的接口

-- 将一个container固化成一个新的iamge(commit)
docker commit <container> [repo:tag]
后面的repo:tag可选
只能提交正在运行的container，即通过docker ps可以看见的容器
查看刚运行的容器

docker ps -l

启动一个已存在的容器（run 是从image新建容器后再启动），以下也可以使用docker start 容器id

```
### 常用的基本操作
容器可以通过run 新建一个来运行，也可以重建start已经停止的container，但start不能够再指定容器启动时运行的指令，因为docker只能有一个前台进程。
容器stop （或 ctrl+d）时，会在保存当前容器的状态之后退出，下次start时保存上次关闭时更改。而且每次进入attach进去的界面是一样的，run启动或commit提交的时刻相同。


#### 启动容器:
    docker run
>docker run -it dzl-docker-fs:ctenos8 /bin/bash
-i: 交互式操作。
-t: 终端。
-d: 不会进入容器。
dzl-docker-fs:ctenos8  镜像。
/bin/bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。
启动一个已经停止的docker容器

docker start <容器 ID>

#### 进入容器:
    docker attach
>docker attach <容器 ID>
注意： 如果从这个容器退出，会导致容器的停止。

    docker exec
>docker exec -it <容器 ID> /bin/bash
推荐大家使用 docker exec 命令，因为此命令会退出容器终端，但不会导致容器的停止。

#### 退出容器:
终端输入
    exit

#### 停止容器:
    docker stop
>docker stop <容器 ID>
停止一个容器


#### 重启容器:
    docker restart
>docker restart <容器 ID>
停止的容器可以通过 docker restart 重启：


#### 查看容器:
    docker ps 
>docker ps 查看正在运行的容器命令
docker ps -a 看所有的容器命令
容器运行时不一定有/bin/bash终端来交互执行top命令，查看container中正在运行的进程，况且还不一定有top命令，这是docker top 就很有用了。实际上在host上使用ps -ef|grep docker也可以看到一组类似的进程信息，把container里的进程看成是host上启动docker的子进程就对了。

#### 后台运行容器:
    docker run -itd --name ubuntu-test ubuntu /bin/bash
>在大部分的场景下，我们希望 docker 的服务是在后台运行的，我们可以过 -d 指定容器的运行模式。
docker run -itd --name ubuntu-test ubuntu /bin/bash
注：加了 -d 参数默认不会进入容器，想要进入容器需要使用指令 docker exec（下面会介绍到）。



####  查看image或container的底层信息（inspect）
docker inspect 
docker inspect <容器 ID>
的对象可以是image、运行中的container和停止的container。

#### 删除容器
删除一个或多个container,image(rm,rmi)
你可能在使用过程中会build或commit许多镜像，无用的镜像需要删除。但删除这些镜像是有一些条件的：

同一个IMAGE ID可能会有多个TAG（可能还在不同的仓库），首先你要根据这些 image names 来删除标签，当删除最后一个tag的时候就会自动删除镜像；
承上，如果要删除的多个IMAGE NAME在同一个REPOSITORY，可以通过docker rmi 来同时删除剩下的TAG；若在不同Repo则还是需要手动逐个删除TAG；
还存在由这个镜像启动的container时（即便已经停止），也无法删除镜像；

删除容器
```
docker rm <container_id/contaner_name>

```
删除所有停止的容器
```
docker rm $(docker ps -a -q)
```
删除镜像
```
docker rmi <image_id/image_name ...>
```

#### 导出和导入容器
导出容器

如果要导出本地某个容器，可以使用 docker export 命令。

    docker export eb8834b54fa5 > ctenos8.tar

导入容器快照
可以使用 docker import 从容器快照文件中再导入为镜像，以下实例将快照文件 ctenos8.tar 导入到镜像 dzl-docker-fs:ctenos8

    cat ctenos8.tar  |  docker import - dzl-docker-fs:ctenos8

#### 数据传输
docker ps 查看容器id为4e444364aa2a
docker cp file id:/路径
如：docker cp firewalld 4e444364aa2a:/root


## docker安装
### x86平台CtenOS8上安装docker
#### 在线安装
旧版本的 Docker 称为 docker 或者 docker-engine，使用以下命令卸载旧版本：
```
yum remove docker docker-client  docker-client-latest  docker-common  docker-latest  docker-latest-logrotate  docker-logrotate  docker-selinux  docker-engine-selinux  docker-engine
```
执行以下命令安装依赖包：
```
yum install -y yum-utils
```
鉴于国内网络问题，强烈建议使用国内源，官方源请在注释中查看。

执行下面的命令添加 yum 软件源：
```
yum-config-manager  --add-repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

$ sudo sed -i 's/download.docker.com/mirrors.aliyun.com\/docker-ce/g' /etc/yum.repos.d/docker-ce.repo
```
如果需要测试版本的 Docker 请执行以下命令：
```
sudo yum-config-manager --enable docker-ce-test 
```

安装docker
更新 yum 软件源缓存，并安装 docker-ce
```
yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin --allowerasing
```

#### 离线安装：
[Centos8 下离线安装部署docker 、docker-compose](https://blog.csdn.net/weixin_43510203/article/details/122164834)

[docker路径](https://download.docker.com/linux/static/stable/x86_64/)
下载docker-20.10.9.tgz 
```
tar -zxvf docker-20.10.9-ce.tgz
```
解压之后的文件复制到 /usr/bin/ 目录下
```
cp docker/* /usr/bin/
```
```
vim /etc/systemd/system/docker.service
```
添加以下内容：
```
[Unit]
Description=Docker Application Container Engine
Documentation=https://docs.docker.com
After=network-online.target firewalld.service
Wants=network-online.target
  
[Service]
Type=notify
# the default is not to use systemd for cgroups because the delegate issues still
# exists and systemd currently does not support the cgroup feature set required
# for containers run by docker
ExecStart=/usr/bin/dockerd --selinux-enabled=false
ExecReload=/bin/kill -s HUP $MAINPID
# Having non-zero Limit*s causes performance problems due to accounting overhead
# in the kernel. We recommend using cgroups to do container-local accounting.
LimitNOFILE=infinity
LimitNPROC=infinity
LimitCORE=infinity
# Uncomment TasksMax if your systemd version supports it.
# Only systemd 226 and above support this version.
#TasksMax=infinity
TimeoutStartSec=0
# set delegate yes so that systemd does not reset the cgroups of docker containers
Delegate=yes
# kill only the docker process, not all processes in the cgroup
KillMode=process
# restart the docker process if it exits prematurely
Restart=on-failure
StartLimitBurst=3
StartLimitInterval=60s
  
[Install]
WantedBy=multi-user.target
```
启动docker
给docker.service文件添加执行权限
```
chmod +x /etc/systemd/system/docker.service
```
重新加载配置文件（每次有修改docker.service文件时都要重新加载下）
```
systemctl daemon-reload  
```
启动docker
```
systemctl start docker
```
设置开机启动
```
systemctl enable docker.service
```
查看docker服务状态
```
systemctl status docker
```

[注册阿里云](https://account.console.aliyun.com/v2/#/home/person)
搜:容器镜像服务->镜像加速器
配置docker源
打开daemon.json
```
vim  /etc/docker/daemon.json
```
插入以下内容
```
{
    "registry-mirrors": [
        "https://d7srj0cy.mirror.aliyuncs.com",
        "http://hub-mirror.c.163.com",
        "https://hub.docker.com/"
    ]
}
```


#重启daemon进程
#重启docker
sudo systemctl daemon-reload
sudo systemctl restart docker

#### docker-compose 离线安装
[首先下载离线文件](https://github.com/docker/compose/releases)
上传至服务器之后，将文件迁移到这个位置将文件转移至/usr/local/bin/
找到：v2.28.0
下载 docker-compose-Linux-x86_64
```
chmod +x docker-compose-Linux-x86_64
mv docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
```
检查状态
```
docker-compose -v
```

##
### arm平台Kylin v10 SP2安装docker




### arm平台Kylin v10 U1 安装docker
[docker源码](https://mirrors.cloud.tencent.com/docker-ce/linux/static/stable/aarch64/)
[银河麒麟操作系统 v10 中离线安装 Docker](https://blog.csdn.net/linmengmeng_1314/article/details/135653694)

## docker构建
### 创建基于ctenos8的docker镜像
#### 1.配置docker源
打开vim /etc/docker/daemon.json
插入以下内容:
```
{
	"registry-mirrors": [
		"https://d7srj0cy.mirror.aliyuncs.com",
		"http://hub-mirror.c.163.com",
		"https://hub.docker.com/"
	]
}
```
重启服务
```
sudo systemctl daemon-reload
sudo systemctl restart docker
```
#### 从远程拉ctenos8的基础镜像
```
docker pull centos:centos8
```
#### 创建docker目录
```
mkdir dzl-docker-fs ; cd  dzl-docker-fs
拷贝yum源
mkdir repo ; cp /etc/yum.repos.d/* repo
```

#### 编写Dockerfile
```
#
# MAINTAINER        dongzl
# DOCKER-VERSION    1.0.0
#
# Dockerizing CentOS8: Dockerfile for building CentOS images
#

# 构建Docker镜像必须要有一个基础镜像，即父镜像(可从官网pull也可自己制作)
FROM       centos:centos8.5.2111
# 指定维护者信息
MAINTAINER dzl

# 设置时区环境变量（ENV环境变量在Dockerfile中可以写多个）
# 这些指定的环境变量，后续可以被RUN指令使用，容器运行起来之后，也可以在容器中获取这些环境变量
ENV TZ "Asia/Shanghai"
ENV TERM xterm

# ADD：添加/拷贝文件到container里面，还有一个拷贝命令是COPY
# 两者的区别如下：
# 前者比后者多两个功能；
#     1. 可直接将url对应的文件直接复制到container里面；
#     2. 如果复制的是tar压缩包文件，用ADD拷贝结束后会自动帮我们解压；
ADD repo/*.repo /etc/yum.repos.d/CentOS-Base.repo

# RUN 后面是要执行的命令，每执行一条指令就是一层，所以Dockerfile采用的是分层的技术
#RUN yum install -y curl wget tar bzip2 unzip vim-enhanced passwd sudo yum-utils hostname net-tools rsync man && \
#    yum install -y gcc gcc-c++ git make automake cmake patch logrotate python-devel libpng-devel libjpeg-devel && \
#    yum install -y --enablerepo=epel pwgen python-pip && \
#    yum clean all

# 安装进程管理工具
RUN pip install supervisor  

# 添加进程管理工具的主配置文件到指定目录下，一般是/etc目录
#ADD supervisord.conf /etc/supervisord.conf  

# 为进程管理工具新建一个目录，用来存放启动其他服务的配置文件
# 新建进程管理日志目录
#RUN mkdir -p /etc/supervisor.conf.d && \    
#    mkdir -p /var/log/supervisor            

EXPOSE 22   # Docker服务器开放的端口，供容器外部连接使用(在启动容器时做端口映射)

CMD ["/bin/bash"]

```

#### 构建docker镜像
```
docker build . -t dzl-docker-fs:ctenos8
```
#### 查看
```
docker image ls
```