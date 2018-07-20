# !/usr/bin/env python
# _*_ coding:utf-8 _*_


import requests
import js2py
import json


def renren_login():
    # 安装 pip install js2py  执行js

    session = requests.session()

    session.headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36",

        # 反爬的参数
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # 创建js的执行环境
    context = js2py.EvalJs()

    # 1.请求 rkey的参数 http://activity.renren.com/livecell/rKey''
    rkey_url = 'http://activity.renren.com/livecell/rKey'
    rkey_data = session.get(rkey_url).content.decode()
    rkey_dict = json.loads(rkey_data)['data']

    context.n = rkey_dict

    # 获取 加密方法 中 必要的js代码

    # biGiint 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js'
    max_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js').content.decode()
    context.execute(max_js)

    # RSA  'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js'
    rsa_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js').content.decode()
    context.execute(rsa_js)

    # 'http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js'
    bar_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js').content.decode()
    context.execute(bar_js)

    # 登录参数 phoneNum password c1 rkey
    context.t = {
        "phoneNum": "mr_mao_hacker@163.com",
        "password": "alarmchime",
        "c1": 0
    }

    #  pwd 加密过js找到  c1:0 rkey
    pwd_js = '''
         t.password = t.password.split("").reverse().join(""),
                    setMaxDigits(130);
                    var o = new RSAKeyPair(n.e,"",n.n)
                      , r = encryptedString(o, t.password);
                    t.password = r,
                    t.rKey = n.rkey
    '''
    context.execute(pwd_js)

    print(context.t)
    print(type(context.t))

    #  content.t  类型 是 js2py的对象
    #  t 转换成字典
    # t.to_dict()

    # 登录网址
    login_url = 'http://activity.renren.com/livecell/ajax/clog'
    result = session.post(login_url, data=context.t.to_dict()).content.decode()
    print(result)


    # 目标网址 'http://activity.renren.com/myprofile'
    response = session.get('http://activity.renren.com/myprofile').content.decode()

    with open('01renren.html','w') as f:
        f.write(response)


if __name__ == '__main__':
    renren_login()
