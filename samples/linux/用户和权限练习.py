练习
目录结构 3个部门  5个员工
/home
    company
        training
            scott
            jack
        market
            janny
            tom
        manager
            king

1 比如training组的人的主目录都在training下
  scott的home 是 /home/company/training/scott
1 同一部门的人可以互相查看各自主目录里的文件
  但不能修改,用户仅能够修改自己的内容
2 不可以查看到其他部门的目录
3 属于manager组的人可以查看所有人的主目录

创建组：
  groupadd training
  groupadd market
  groupadd manage
创建组目录：为了目录结构更清晰
  mkdir /home/training
  mkdir /home/market
  mkdir /home/manage
创建用户：
  useradd scott -aG training –d /home/company/training/scott
  useradd jack -aG training –d /home/company/training/jack
  useradd janny -aG market –d /home/company/market/janny
  useradd tom -aG market –d /home/company/market/tom
  useradd  king -aG manage,training,market –d /home/company/manage/king 
# manage可以查看其他成员的文件

设置登录密码
  passwd scott 
  passwd jack
  passwd janny 
  passwd tom 
  passwd king 

同一组的用户能互相访问：
改文件夹所属组
  chgrp –R training /home/training  
  chgrp –R market /home/market
  chgrp –R manage /home/manage
改文件夹权限
  chmod g+rx /home/training -R    # 文件夹权限中的x能cd  r能ls
  chmod g+rx /home/market –R
  chmod g+rx /home/manage –R
  chmod o-x /home/training # 不能被其他部门访问
  chmod o-x /home/market
  chmod o-x /home/manage
