#!/bin/bash
#author
#tel


#打包代码
tar_code(){
    #远程调用代码托管服务器 /data/scripts/tar_code_pro.sh
    echo "正在打包代码...."
    ssh root@192.168.16.77 "bash /data/scripts/tar_code_pro.sh"


}


#传输代码
transport_code(){
    echo "代码正在传输中...."


}


#解压代码
untar_code(){
    echo "代码正在解压中...."


}



#停止服务
stop_server(){
    echo "正在停止nginx服务器...."
    echo "正在停止django服务"


}



#备份代码
backup_code(){
    echo "代码正在备份...."


}



#更新代码
update_code(){
    echo "代码正在更新中...."


}


#重启服务
restart_server(){
    echo "正在启动django服务...."
    echo "正在启动nginx服务"


}

#检查
check(){
    echo "长在检查更新...."


}


tar_code
transport_code
untar_code
stop_server
backup_code
update_code
restart_server
check