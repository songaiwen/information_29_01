"""
1.grep命令详解
    grep命令是我们常用的一个强大的文本搜索命令
        grep [参数] [关键字] <文件名>
    注意： 我们在查看某个文件的内容的时候，是需要有<文件名> grep命令在结合|(管道符)使用的情况下，后面的<文件名>是没有的

    参数详解:
    -c：只输出匹配行的计数。
    -n：显示匹配行及行号。
    -v：显示不包含匹配文本的所有行。
    也可以结合同时使用-cv  -nv

    模板文件:
        admin-1@ubuntu:~$ cat find.txt
        nihao aaa
        nihao AAA
        NiHao bbb
        nihao CCC

            -c: 输出匹配到aaa的个数
            admin-1@ubuntu:~$ grep -c aaa find.txt
            1

            -n: 输出匹配内容，同时显示行号
            admin-1@ubuntu:~$ grep -n CCC find.txt
            4:nihao CCC

            -v: 匹配到的内容部输出，输出不匹配的内容
            admin-1@ubuntu:~$ grep -v ni find.txt
            NiHao bbb

        小技巧： 精确定位错误代码
        grep -nr [错误关键字] *

2.sed命令详解
    1.sed行文件编辑工具,编辑文件是以行为单位的
        命令格式:sed [参数] '<匹配条件> [动作]' [文件名]
        -i 表示对文件进行编辑(不添加-i参数，修改操作结果直接往屏幕输出，不修改原文件)

    2.匹配条件分为两种:数字行号或者关键字匹配
        关键字匹配'/关键字/' 可以更换成@＃! 等符号  如果关键字和隔离符号冲突,更换成其他的符号即可
        动作详解
            -a 在匹配到的内容下一行增加内容
            -i 在匹配到的内容上一行增加内容
            -d 删除匹配到的内容
            -s 替换匹配到的内容
            注意：上面的动作应该在参数为-i的时候使用，不然的话不会修改原文件


        替换操作 主要参数：行号，列号，全体
            格式：
            命令格式：sed -i [替换格式] [文件名]
            替换格式：'s#原内容#替换后内容#'

        准备文件:
            admin-1@ubuntu:~$ cat sed.txt
            nihao sed sed sed
            nihao sed sed sed
            nihao sed sed sed
            替换每行首个匹配内容：sed -i 's#原内容#替换后内容#' 文件名
            示例：替换首每行的第1个sed为SED
            admin-1@ubuntu:~$ sed -i 's#sed#SED#' sed.txt


            替换全部匹配内容：sed -i 's#原内容#替换后内容#g' 文件名  g表示的全部替换
            示例：替换全部sed为des
            admin-1@ubuntu:~$ sed -i 's#sed#SED#g' sed.txt
            admin-1@ubuntu:~$ cat sed.txt
            nihao SED SED SED
            nihao SED SED SED
            nihao SED SED SED

            指定行号替换首个匹配内容：sed -i '行号s#原内容#替换后内容#' 文件名
            示例：替换第2行的首个SED为sed
            admin-1@ubuntu:~$ sed -i '2s#SED#sed#' sed.txt
            admin-1@ubuntu:~$ cat sed.txt
            nihao SED SED SED
            nihao sed SED SED
            nihao SED SED SED


            首行指定列号替换匹配内容：sed -i 's#原内容#替换后内容#列号' 文件名
            示例：替换每行的第2个SED为sed
            admin-1@ubuntu:~$ sed -i 's#SED#sed#2' sed.txt
            admin-1@ubuntu:~$ cat sed.txt
            nihao SED sed SED
            nihao sed SED sed
            nihao SED sed SED

            指定行号列号匹配内容：sed -i '行号s#原内容#替换后内容#列号' 文件名
            示例：替换第3行的第2个SED为sed
            admin-1@ubuntu:~$ sed -i '3s#SED#sed#2' sed.txt
            admin-1@ubuntu:~$ cat sed.txt
            nihao SED sed SED
            nihao sed SED sed
            nihao SED sed sed

    3.追加操作:在指定行号的下一行增加内容
        格式：sed -i '行号a\增加的内容' 文件名
        注意：如果增加多行，可以在行号位置写个范围值，彼此间使用逗号隔开
        sed -i '1,3a\增加内容' 文件名

        指定行号增加内容
        admin-1@ubuntu:~$ sed -i '2a\zengjia-2' sed.txt
        admin-1@ubuntu:~$ cat sed.txt
        nihao SED sed SED
        nihao sed SED sed
        zengjia-2
        nihao SED sed sed


        指定1~3每行都增加内容
        admin-1@ubuntu:~$ sed -i '1,3a\tongshi-2' sed.txt
        admin-1@ubuntu:~$ cat sed.txt
        nihao SED sed SED
        tongshi-2
        nihao sed SED sed
        tongshi-2
        zengjia-2
        tongshi-2
        nihao SED sed sed

    4.插入操作:在指定行号的当行增加内容
        格式：sed -i '行号i\增加的内容' 文件名
        注意：如果增加多行，可以在行号位置写个范围值，彼此间使用逗号隔开
        指定行号增加内容
        admin-1@ubuntu:~$ sed -i '1i\insert-1' sed.txt
        admin-1@ubuntu:~$ cat sed.txt
        insert-1
        nihao SED sed SED
        tongshi-2
        nihao sed SED sed
        tongshi-2
        zengjia-2
        tongshi-2
        nihao SED sed sed

    5.删除操作:指定行号删除
        格式：sed -i '行号d' 文件名
        注意：如果删除多行，可以在行号位置多写几个行号，彼此间使用逗号隔开
        删除第4行内容
        admin-1@ubuntu:~$ sed -i '4d' sed.txt
        admin-1@ubuntu:~$ cat sed.txt
        insert-1
        nihao SED sed SED
        tongshi-2
        tongshi-2
        zengjia-2
        tongshi-2
        nihao SED sed sed

        删除多行(3-5行)内容
        admin-1@ubuntu:~$ sed -i '3,5d' sed.txt
        admin-1@ubuntu:~$ cat sed.txt
        insert-1
        nihao SED sed SED
        tongshi-2
        nihao SED sed sed


3.awk命令详解
    awk是一个功能非常强大的文档编辑工具，它不仅能以行为单位还能以列为单位处理文件。
    命令格式： awk [参数] '[ 动作]' [文件名]
    常见参数：
    -F 指定行的分隔符

    常见动作：
    print 显示内容
    $0 显示当前行所有内容
    $n 显示当前行的第n列内容，如果存在多个$n，它们之间使用逗号(,)隔开

    常见内置变量
    FILENAME 当前输入文件的文件名，该变量是只读的
    NR 指定显示行的行号
    NF 输出 最后一列的内容
    OFS 输出格式的列分隔符，缺省是空格
    FS 输入文件的列分融符，缺省是连续的空格和Tab 模板文件内容

    demo:
    admin-1@ubuntu:~$ cat awk.txt
    nihao awk awk awk
    nihao awk awk awk

    1.打印第1列的内容
        admin-1@ubuntu:~$ awk '{print $1}' awk.txt
        nihao
        nihao
    2.打印第一行第1和第3列内容
        admin-1@ubuntu:~$ awk  'NR==1 {print $1,$3}' awk.txt
        nihao awk

    3.指定隔离分隔符，查看内容
        admin-1@ubuntu:~$ cat linshi.txt
        root:x:0:0:root:/root:/bin/bash
        admin-1@ubuntu:~$ awk -F ':' '{print $1,$7}' linshi.txt
        root /bin/bash

    4.设置显示分隔符，显示内容
        admin-1@ubuntu:~$ awk 'BEGIN{OFS=":"} {print NR,$0}' awk.txt
        1:nihao awk awk awk
        2:nihao awk awk awk

4.find命令详解
    命令格式： find [路径] [参数] [关键字] 参数详解
    -name 按照文件名查找文件。
    -perm 按照文件权限来查找文件。
    -user 按照文件属主来查找文件。
    -group 按照文件所属的组来查找文件。
    -type 查找某一类型的文件 文件类型诸如：
    b - 块设备文件
    d - 目录
    c - 字符设备文件
    p - 管道文件
    l - 符号链接文件
    f - 普通文件。
    -size n：[c] 查找文件长度为n块的文件，带有c时表示文件长度以字节计。
    -depth：在查找文件时，首先查找当前目录中的文件，然后再在其子目录中查找。
    -mindepth n：在查找文件时，查找当前目录中的第n层目录的文件，然后再在其子目录中查找。
    ! : 表示取反 命令演示: 在当前系统中查找一个叫awk的文件
    admin-1@ubuntu:~$ sudo find /home/admin-1/ -name "awk.txt"
    /home/admin-1/awk.txt
    在当前系统中查找文件类型为普通文件的文件
    admin-1@ubuntu:~$ find /tmp -type f
    /tmp/.X0-lock
    /tmp/vgauthsvclog.txt.0
    /tmp/unity_support_test.0
    /tmp/config-err-4igbXW
"""