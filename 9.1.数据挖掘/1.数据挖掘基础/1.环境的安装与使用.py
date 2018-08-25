"""
1.创建虚拟环境 mkvirtualenv -p python3  ai

2.安装
    matplotlib==2.2.2
    numpy==1.14.2
    pandas==0.20.3
    TA-Lib==0.4.16
    tables==3.4.2
    jupyter==1.0.0

3.Ta-Lib安装会出现问题，需要先安装依赖库，按照以下步骤安装：

        # 获取源码库
        sudo wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
        # 解压进入目录
        tar -zxvf ta-lib-0.4.0-src.tar.gz
        cd ta-lib/
        # 编译安装
        sudo ./configure --prefix=/usr
        sudo make
        sudo make install
        # 重新安装python的TA-Lib库
        pip install TA-Lib

4.pip install -r requirements.txt

5.Jupyter Notebook介绍
Jupyter项目是一个非盈利的开源项目，源于2014年的ipython项目，
因为它逐渐发展为支持跨所有编程语言的交互式数据科学和科学计算

    Jupyter Notebook，原名IPython Notbook，是IPython的加强网页版，一个开源Web应用程序
    名字源自Julia、Python 和 R（数据科学的三种开源语言）
    是一款程序员和科学工作者的编程/文档/笔记/展示软件
    .ipynb文件格式是用于计算型叙述的JSON文档格式的正式规范

6.为什么使用jupyter notebook
    传统软件开发：工程／目标明确
        需求分析，设计架构，开发模块，测试
    数据挖掘：艺术／目标不明确
        目的是具体的洞察目标，而不是机械的完成任务
        通过执行代码来理解问题
        迭代式地改进代码来改进解决方法
    总结:jupyter notebook相比pycharm在画图和数据战士方面更有优势

7.jupyter notebook的使用
    进入虚拟环境以后workon  ai
    输入命令  jupyter notebook 默认打开一个url为http://localhost:8888网页版
    新建notebook文档,文档格式是.ipynb
    标题栏:点击标题修改文档名
    导航File  ----> Download as 是另存为其他格式
    导航Kernel中有以下功能:
        Interrupt，中断代码执行（程序卡死时）
        Restart，重启Python内核（执行太慢时重置全部资源）
        Restart & Clear Output，重启并清除所有输出
        Restart & Run All，重启并重新运行所有代码

8.cell操作
    一对In  Out会话被视作一个代码单元,称为cell
    jupyter支持的哦是
        编辑模式（Enter）
            命令模式下回车Enter或鼠标双击cell进入编辑模式
            可以操作cell内文本或代码，剪切／复制／粘贴移动等操作
        命令模式（Esc）
            按Esc退出编辑，进入命令模式
            可以操作cell单元本身进行剪切／复制／粘贴／移动等操作

9.快捷键操作
    shift+enter 代表执行单元代码,并跳转到下一单元
    ctrl+enter 代表执行本单元代码,留在本单元


    cell行号前的 * ，表示代码正在运行

        命令模式：按ESC进入
            Y，cell切换到Code模式
            M，cell切换到Markdown模式
            A，在当前cell的上面添加cell
            B，在当前cell的下面添加cell
            双击D：删除当前cell
            Z，回退
            L，为当前cell加上行号 <!--
            Ctrl+Shift+P，对话框输入命令直接运行
            快速跳转到首个cell，Crtl+Home
            快速跳转到最后一个cell，Crtl+End -->
        编辑模式：按Enter进入
            多光标操作：Ctrl键点击鼠标（Mac:CMD+点击鼠标）
            回退：Ctrl+Z（Mac:CMD+Z）
            重做：Ctrl+Y（Mac:CMD+Y)
            补全代码：变量、方法后跟Tab键
            为一行或多行代码添加/取消注释：Ctrl+/（Mac:CMD+/）
            屏蔽自动输出信息：可在最后一条语句之后加一个分号


10.markdown演示
    #一级标题
    ##二级标题
    ###三级标题
    ####四级标题
    #####五级标题
    - 缩进
        - 二级缩进
            - 三级缩进

"""