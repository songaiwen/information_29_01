# __init__.py: 控制包导入模块的行为
# 指定from 包名 import * 可以导入包里面那些模块
__all__ = ["recv_msg"]
# 从包里面导入指定模块
from first_package import recv_msg
# .表示当前包
from . import send_msg