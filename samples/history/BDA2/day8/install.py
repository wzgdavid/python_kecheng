Centos下安装
先安装yum安装openssl-devel ，否则pip不能安装，或会出现ssl错误
1.发现缺少openssl-devel包 

yum安装openssl-devel 
[root@localhost ~]# yum install openssl-devel -y

 2 ，安装python3
 
 # su root     用root安装，权限问题  

$ wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
解压 ,也可右键解压
# tar zxvf Python-3.6.1.tgz
cd到前面那个解压出来的目录
# cd Python-3.6.1
依次执行以下三条命令
 
# ./configure
# make
# make install
 
命令行中输入python3，进入python交互，安装成功
 
3，  安装pycharm
 
http://www.jetbrains.com/pycharm/download/#section=linux，选Community版本
这时不用root，切回自己的user
下载，解压，然后cd到解压好的目录下的bin，然后./pycharm.sh启动
 
 
4，pycharm选python3环境
打开pycharm，菜单选File  ---- New project，出现对话框，点下拉框右边的齿轮状图标，点add local，目录中选 之前安装python3的目录下的python，比如 home/Python-3.6.1/python
 
 
 
 
 
安装sublime text2，运行python3
菜单选择tools-->build System-->new build system
在打开的文件中贴入以下内容，注意cmd后的路径，是自己安装的目录中的python，
{
    "cmd": ["/home/wzg/Python-3.6.1/python","-u","$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python"
}
文件名存为python3.sublime-build
然后tools-->build system, 选择python3，就是上面保存的名字
 
tab设置为4个空格
Preferences-->Settings Default 打开的文件中
"tab_size": 4,
"translate_tabs_to_spaces": true, 


安装scikit-learn准备工作
直接pip3 install scikit-learn能安装成功，但是import sklearn ,就会报错
ImportError: no module named '_bz2'
 
解决办法
yum install bzip2-devel

安装matplotlib准备工作
在centos系统下，导入matplotlib时，出现ImportError: No module named '_tkinter'的错误，首先yum list installed | grep ^tk 
查看是否存在相应模块，通常原因是tkinter和tk-devel缺失。通过yum install -y tkinter和yum install -y tk-devel下载相应模块，

以上准备工作都弄好之后，再编译Python（不用弄一次编译一次）。先cd到自己的python安装目录，编译代码如下：
./configure
make
make install






windows下安装
安装python3
去官方地址：https://www.python.org/   下载，下载下来的exe文件直接安装，然后看看系统环境变量有没有添加刚才安装的python目录，有两个，没有就手动添加
比如D:\Python36\Scripts\;D:\Python36\;

安装numpy等库
先安装wheel，
pip3 install wheel  # pip3对应安装的python3
pip3 uninstall xxx  # 安装失败的删除
然后去
http://www.lfd.uci.edu/~gohlke/pythonlibs/
–下载对应版本numpy+mkl的whl文件，然后本地安装whl
pip3 install 下载的本地whl文件
Python32位还是64位可以看这里
Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
后面的库pandas，scipy,scikit-learn,matplotlib，如果直接pip安装有问题的话，都用以上安装方法


