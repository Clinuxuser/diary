制造rpm包
---------

安装软件
~~~~~~~~

yum -y install rpm-build yum install rpmdevtools

配置工作环境
~~~~~~~~~~~~

执行\ ``rpmdev-setuptree``\ 命令（rpmdevtools的命令），设置工作空间。
行了这个命令之后，在root目录下多了一个rpmbuild的文件夹，里边内容如下（具体介绍见后文，此处仅做流程演示）：

::

   $ tree rpmbuild
   rpmbuild
   ├── BUILD
   ├── RPMS
   ├── SOURCES
   ├── SPECS
   └── SRPMS

或者执行以下命令：

::

   mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

源代码tar包或者tar.gz放入SOURCES文件夹下。

其中，“宏代码”这一列就可以在SPEC文件中用来代指所对应的目录，类似于编程语言中的宏或全局变量。当然~/rpmbuild这个文件夹也是有宏代码的，叫做%_topdir

编写配置文件
~~~~~~~~~~~~

编写SPEC文件
^^^^^^^^^^^^

::

   vim soft.spec

::

   Name:
   Version:
   Release:        1%{?dist}
   Summary:

   Group:
   License:
   URL:
   Source0:

   BuildRequires:
   Requires:

   %description


   %prep
   %setup -q


   %build
   %configure
   make %{?_smp_mflags}


   %install
   %make_install


   %files
   %doc



   %changelog

修改

::

   # RPM package spec file for "example-package"
   # Replace "example-package" with your actual package name

   # Define the basic information about the package
   Name:           example-package
   Version:        1.0
   Release:        1%{?dist}
   Summary:        A simple example package

   # The License field indicates the software's license
   License:        GPLv3+
   URL:            https://www.example.com
   Source0:        %{name}-%{version}.tar.gz

   # Define the build requirements and dependencies
   BuildRequires:  gcc
   BuildRequires:  make

   # The BuildArch field specifies the target architecture
   # If the package is architecture-independent, use "noarch"
   BuildArch:      x86_64

   # The %description section provides a brief description of the package
   %description
   This is an example package to demonstrate creating RPM packages.

   # The %prep section extracts the source code from the tarball
   %prep
   %autosetup -n %{name}-%{version}

   # The %build section contains the build commands
   %build
   %configure
   make %{?_smp_mflags}

   # The %install section installs the built files to the BUILDROOT directory
   %install
   make install DESTDIR=%{buildroot}

   # The %files section lists all the files and directories to be packaged
   %files
   %{_bindir}/your_executable_binary
   %{_mandir}/man1/your_manpage.1.gz
   /etc/your_config.conf

   # The %changelog section is for recording changes to the package over time
   %changelog
   * Mon Jul 01 2023 Your Name <your.email@example.com> - 1.0-1
   - Initial package release

然后 :wq保存即可。

制作
^^^^

rpmbuild -ba –nodebuginfo soft.spec

demo:cjson
~~~~~~~~~~

执行：rpmdev-setuptree创造工作空间

在SOURCES目录下存在一个libcJSON-1.3.2.tar.gz文件
并且该压缩包解析之后为libcJSON-1.3.2目录

vim SPECS/soft.spec

::

   Name: libcJSON 
   Version: 1.3.2 
   Release: 1%{?dist}
   Summary: The WT cJSON C library

   Group: Development/Libraries 
   License: GPLv3+ 
   URL: https://github.com/arnoldlu/cJSON 
   Source0: %{name}-%{version}.tar.gz

   BuildRequires: gcc 
   Requires: make 

   BuildArch:      x86_64

   %description
   https://github.com/arnoldlu/cJSON


   %prep
   %setup -q


   %build
   make -j10 %{?_smp_mflags}


   %install
   %make_install


   %files
   %doc
   %{_prefix}/local/include/cjson/
   %{_prefix}/local/lib/



   %changelog

执行构建命令： rpmbuild -ba –nodebuginfo soft.spec
