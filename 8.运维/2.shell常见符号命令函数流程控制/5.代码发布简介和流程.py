"""
1.什么是代码发布?
    代码发布是：将代码放到互联网服务器上，对外提供web服务。
    发布什么?
    ​ 代码 经过测试，功能完善，没有问题的代码

    发布到哪里?
    ​ 服务器 所有人都能访问的到的一台服务器(有公网IP)

    ​ idc机房、阿里云、亚马逊、腾讯云、华为云、...

    发布的效果?
    ​ web网页对外展示

2.发布方式:手工发布代码, 脚本发布代码

3.代码发布的流程
    获取代码--->从个人电脑中上传到部署了gitlab服务的linux主机  集中式的:svn  和分布式的git
    打包代码--->  tar和zip   windows使用zip和rar
    传输代码--->git和scp,ftp,共享挂载cp, rsync
    停止应用--->nginx 和 django web 应该先停距离用户最近的nginx服务,然后再停web服务
    解压代码--->
    放置代码--->
    开启应用--->先开启距离用户远的,先开启django Web服务  然后再开启nginx
    检查效果--->
    对外访问

4.文件压缩和解压缩
    tar zcvf test.tar.gz test
    tar xf test.tar.gz
    查看压缩文件内容
    zcat 压缩文件


5.文件传输
    文件的传输

​     scp传输工具：

​         命令格式：scp 源文件 目标位置

​     将本地文件推送到远程主机

​         scp python.tar.gz root@192.168.8.15:/root/

​     将远程主机的文件拉取到本地

​         scp root@192.168.8.15:/root/python.tar.gz ./

​     远端主机文件夹位置的表示形式：

​         远程连接的用户@远程主机:远程主机的目录路径

​     远端主机文件位置的表示形式：

​         远程连接的用户@远程主机:远程主机的文件路径

6.文件备份:要有一定的标志符号，目前通用的是使用时间戳的形式来表示
    date命令详解：命令格式：date [option]


    参数	作用
    %F	显示当前日期格式，%Y-%m-%d
    %T	显示当前时间格式，%H:%M:%S

    python@ubuntu:~/shell/day2$ date +%F
    2018-08-12
    python@ubuntu:~/shell/day2$ date +%F%T
    2018-08-1214:07:14
    python@ubuntu:~/shell/day2$ date "+%F %T"
    2018-08-12 14:07:37
    python@ubuntu:~/shell/day2$


      指定时间戳格式：

      年月日时分秒：date +%Y%m%d%H%M%S

  备份命令效果格式：

      方式一：复制备份
          cp nihao nihao-$(date +%Y%m%d%H%M%S)

      方式二：移动备份
          mv nihao nihao-$(date +%Y%m%d%H%M%S)


"""