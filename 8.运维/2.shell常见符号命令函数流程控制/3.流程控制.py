"""
1.单分之if语句
    语法格式
        if [ 条件 ]
        then
             指令
        fi
    单一条件,只是一个输出
    #!/bin/bash
    $arg1 = $1
    if [ $arg1 == "秩序白银" ]
    then
        echo "初级玩家"
    fi


2.双分支if语句
    if [ 条件 ]
    then
         指令1
    else
        指令2
    fi

3.多分支if语句
    admin-1@ubuntu:/data/scripts/python-n# cat if.sh
    #!/bin/bash
    # 多if语句的使用场景
    if [ "$1" == "start" ]
    then
       echo "服务启动中..."
    elif [ "$1" == "stop" ]
    then
       echo "服务关闭中..."
    elif [ "$1" == "restart" ]
    then
       echo "服务重启中..."
    else
       echo "$0 脚本的使用方式： $0 [ start | stop | restart ]"
    fi


4.case选择语句
    格式
    case 变量名 in
       值1)
          指令1
             ;;
       ...
       值n)
         指令n
             ;;
    esac

    注意：首行关键字是case，末行关键字esac选择项后面都有 )每个选择的执行语句结尾都有两个分号;

    服务器启动demo
    # cat case.sh
    #!/bin/bash
    # case语句使用场景
    case "$1" in
        "start")
            echo "服务启动中..."
            ;;
        "stop")
            echo "服务关闭中..."
            ;;
        "restart")
            echo "服务重启中..."
            ;;
        *)
            echo "$0 脚本的使用方式： $0 [ start | stop | restart ]"
            ;;
    esac


5.for循环语句
    for 值 in 列表
    do
       执行语句
    done

      1 #!/bin/bash
      2
      3 for item in $(ls ./)
      4 do
      5     echo $item
      6 done


6.while 循环语句

    语法格式
    while 条件
    do
       执行语句
    done

      1 #!/bin/bash
      2
      3 n=0
      4 while [ $n -le 5 ]
      5 do
      6     echo $n
      7     let n+=1
      8 done


7.until循环语句 :直到......为止, 只要不满足条件我就一直做事情,但是条件满足就结束循环
    until 条件
    do
       执行语句
    done


    #!/bin/bash
    # until的示例
    a=1
    until [ "${a}" -eq 5 ]
    do
       echo "${a}"
       a=$((a+1))
    done
"""