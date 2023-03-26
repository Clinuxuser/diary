文档编写指南
############################################


一、安装sphinx
********************************************
::

    yum install python3
    pip3 install -U Sphinx  

二、搭建工程    
********************************************

1. 创建工程
============================================
| 执行命令创建工程:

.. code-block:: 

    sphinx-quickstart

| 是否创建工程: 

.. code-block:: 
    
    Separate source and build directories (y/n) [n]: y

| 项目名称：demo 

.. code-block:: 
    
    Project name:demo

| 用户名称：dongzl 

.. code-block:: 

    Author name(s):dongzl 

| 工程版本：v1.0

.. code-block:: 

    Project release []: v1.0

| 支持语言：中文简体

.. code-block:: 

    Project language [en]:zh_CN 

2. 目录结构
============================================
目录结构为：

.. code-block:: 
    
    [root@bogon demo]# tree
    .
    ├── build
    ├── make.bat
    ├── Makefile
    └── source
        ├── conf.py
        ├── index.rst
        ├── _static
        └── _templates

source：源文件存放目录    
build编译生成文件的存放目录    
Makefile：Linux下的makefile。    
make.bat：Windows下的makefile。       
conf.py：配置文件  
index.rst：主框架文件  
_static：静态文件存放目录，比如可以放一些图片什么的  
_templates：模板存放目录。  

3. conf.py配置
============================================
3.1 主题样式 :
--------------------------------------------
| 默认的主题是alabaster 
| 设置alabaster主题只需在html_theme中设置名字即可 

:: 

    html_theme = 'alabaster' 

| 如果想安装其它的主题，可以先到Sphinx的官网https://sphinx-themes.org/查看.  
| 这里选用一个较为常用的主题Read the Docs，安装这个主题首先需要在python中进行安装，命令如下：

:: 

    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx_rtd_theme

| 要设置sphinx_rtd_theme主题，需要在文件头部加上:     
    
:: 

    import sphinx_rtd_theme

| 再设置html_theme:  

::

    html_theme = 'sphinx_rtd_theme' 


3.2 设置图片logo：
--------------------------------------------
| 在html_logo中设置图片文件路径:  

::

    html_logo = './demo/image/logo.jpg'

3.3 不显示源文件链接
--------------------------------------------
| 默认会在生成的html页中显示rst源文件链接，做如下设置后不显示:  

::

    html_show_sourcelink = False

3.4 index页配置
--------------------------------------------
| 主要是设置目录树:

.. code-block::

        .. toctree::
        :maxdepth: 3
        :numbered:

        foo
        bar

| maxdepth把index.html页中目录的标题显示深度限制设为3，numbered为编号。之后空一行，在下面列出各子文档，可以不加文件后缀。 [#f1]_ 

.. [#f1] 注：在这里同样要注意代码对齐

4. 安装markdown支持工具
============================================
| 如果相要使用markdown格式的文档，还要安装markdown支持工具，命令如下： 

::

    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple recommonmark

| 若要使用markdown的表格，还要安装：

:: 

    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sphinx_markdown_tables

| 然后，还要修改conf.py 文件，找到 extensions字段，修改为 [#f2]_ :  

::

    extensions = ['recommonmark','sphinx_markdown_tables']

| markdown格式的文件不能通过Read the Docs校验

.. [#f2] 注：支持markdown后，文档文件可以使用markdown格式，但文档的配置文件index.rst还要使用reST格式


5. 添加文件
============================================
| 在source目录下创建demo目录，将要添加的数据信息存放到该目录下。    
| 在demo目录下创建image目录和file  
| image：存放图片文件  
| file：存放任意文件  
| 在file目录下创建intro.rst和sample.md [#f3]_

.. [#f3]  注:默认支持.rst格式文件，安装完markdown之后支持.md文件 且语法需要正确

目录结构：

::

    .
    ├── file
    │   ├── intro.rst
    │   └── sample.md
    └── img
        └── logo.jpg

6. index.rst 配置
============================================

::

    .. demo documentation master file, created by
    sphinx-quickstart on Sun Mar 26 00:33:56 2023.
    You can adapt this file completely to your liking, but it should at least
    contain the root `toctree` directive.

    Welcome to demo's documentation!
    ================================

    .. toctree::
    :maxdepth: 3
    :caption: Contents:

    ./demo/file/intro
    ./demo/file/sample

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`


7. 编译
============================================
| 配置完成之后进行编译： 

::

    make html

| 生成的html为build/html目录下的index.html

三、文档托管
********************************************
1. 上传 GitHub
============================================
* 首先在 GitHub 上创建一个 diary 仓库。
* 在本地 diary 目录中添加 README.md 和 .gitignore 文件，在 .gitignore 文件中写入下面一行。

::

    build/

| 表示不跟踪 build 目录，因为我们后面将使用 Read the Docs 进行文档的构建和托管。

* 将创建的工程上传到 `GitHub <https://github.com/>` 

2.网页托管
============================================
| 在 `阅读文档 <https://readthedocs.org/>`_ 网站 https://readthedocs.org/ 注册，并绑定 GitHub 账户。点击“Import a Project”导入项目，输入项目名称和仓库地址即可 [#f4]_

.. [#f4] 该网页不支持markdown格式的文件。

| 将生成的网页粘贴到项目上的README
