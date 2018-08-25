"""
1.函数的格式和调用
    #!/bin/bash
    # 函数使用场景一：执行频繁的命令
    dayin(){
      echo "wo de mingzi shi  111"
    }
    # 调用
    dayin


2.函数传参和函数体内调用参数示例
    #!/bin/bash

    dayin(){
      echo "wo de mingzi shi $1"
    }
    # 调用函数传参
    dayin 111

3. 脚本传参
    #!/bin/bash
    # 定义传参数函数
    dayin(){
      echo "wode mignzi shi $1"
    }
    # 调用函数传参
    dayin $1

4.脚本传参函数调用(生产用)
    #!/bin/bash
    # 函数的使用场景二
    canshu = "$1"
    dayin(){
      echo "wo de mingzi shi $1"
    }
    # 调用函数传参
    dayin "${canshu}"
"""