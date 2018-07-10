import requests

def renren_profile():
    #1.url目标  人人好友页面

    # profile_url = "http://www.renren.com/346111031/profile"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }
    #1.代码实现登陆,只要登陆成功cookie有效
    #2.找到登陆url
        #找form标签,action = "目标url"
        #如果没有action;抓包,跳转刷新 勾选preserve log
    login_url = 'http://www.renren.com/PLogin.do'
    #3.拼接登陆的参数
    login_data = {
        "email":"576883213@qq.com",
        "password":"912719"
    }
    #4.发送登陆请求post
        #session对象,自动保存cookit
    session = requests.session()
    session.post(login_url, headers=headers, data=login_data)
    #5.如果成功,
    # 1.url 目标 人人好友页面
    profile_url = "http://www.renren.com/346111031/profile"

    data = session.get(profile_url, headers=headers).content.decode()
    with open("02renren3.html", 'w') as f:
        f.write(data)

if __name__ == '__main__':
    renren_profile()