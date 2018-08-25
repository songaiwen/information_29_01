"""
1.重定向符号
    在shell脚本中有两种常见的重定向符号>和 >>
    ">" 符号作用:表示就爱那个符号左侧的内容或者输出结果,以覆盖的方式输入到右侧文件中
    ">>" 符号 作用： ">>" 表示将符号左侧的内容，以追加的方式输入到右侧文件的末尾行中 查看文件内容


2.管道符 |
    是传递信息使用的  命令1  |  命令2
    管道左侧命令1执行后的结果作为输入传递给右侧的命令2使用

    命令演示： 查看当前系统中的全局变量SHELL
    admin-1@ubuntu:~$ env | grep SHELL
    SHELL=/bin/bash

    ps ajx  查询出很多正在运行的程序   可以使用管道进行条件查询  ps ajx | grep 进程号

3.其他符号
    1.后台展示符号& (跟在一条命令之后,将一个命令从前台转到后台执行)
        命令 & 使用sleep命令使终端界面阻塞4秒,使用当前进程执行
        admin-1@ubuntu:~# sleep 10 &
        [1] 4198
        admin-1@ubuntu:~# ps aux | grep sleep
        root       4198  0.0  0.0   9032   808 pts/17   S    21:58   0:00 sleep 10
        root       4200  0.0  0.0  15964   944 pts/17   S+   21:58   0:00 grep --color=auto sleep

    2.全部信息符号
        全部信息符号 2>&1 符号详解： 1 表示标准输出的信息 2 表示标准错误的信息 2>&1 代表所有输出的信息 符号示例 标准正确输出示例
        demo
        定义文件demo.sh
            #!/bin/bash
            echo "hello world"
            jfkljfdljfkdjflkadsj
        执行结果
            python@ubuntu:~/shell/day2$ bash demo.sh 1 >> ok.txt
            3.std.sh: 行 6: jfkljfdljfkdjflkadsj: 未找到命令

            python@ubuntu:~/shell/day2$ bash 3.std.sh 2>> error.txt
            hello world

        将所有的信息都重定向到一个文件里面
            python@ubuntu:~/shell/day2$ bash 3.std.sh >> all.txt 2>&1
            python@ubuntu:~/shell/day2$ cat all.txt
            hello world
            3.std.sh: 行 6: jfkljfdljfkdjflkadsj: 未找到命令
            hello world
            3.std.sh: 行 6: jfkljfdljfkdjflkadsj: 未找到命令
            python@ubuntu:~/shell/day2$
        将所有的信息重定向到黑洞null里面,同时是在后台运行用&结尾
            python@ubuntu:~/shell/day2$ bash 3.std.sh >> /dev/null 2>&1 &
            [1] 23781





"""