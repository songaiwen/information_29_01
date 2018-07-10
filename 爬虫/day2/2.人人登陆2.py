import requests

def renren_profile():
    #1.url目标  人人好友页面

    profile_url = "http://www.renren.com/346111031/profile"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }

    #2.通过cookie参数传递 型式是字典
    cook_str = 'anonymid=j2ugvrvr-u09ui9; depovince=BJ; _r01_=1; JSESSIONID=abcrNRGNH2FBMgrjke_rw; ick_login=7aad3f95-8ef4-4d63-b328-1bea2307db99; _de=5B6A20C030F5671D340E4CEC836F3769696BF75400CE19CC; first_login_flag=1; ln_uact=576883213@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20121210/0935/h_main_2cyU_36ec00005b8b1375.jpg; id=501025059; loginfrom=syshome; jebe_key=4fb84a06-713b-4f42-ba8a-66598d1ced5b%7Cd9b53598af5070689701c29f5dd59698%7C1531123430038%7C1%7C1531123430208; wp_fold=0; jebecookies=571408f7-17a4-412f-91b8-d76c2448f661|||||; p=9f8d1aac3a98b126d55ad8006ec4551f9; t=29d1b5a59b00dc38b1f563479462d5fe9; societyguester=29d1b5a59b00dc38b1f563479462d5fe9; xnsid=7e35d92d; XNESSESSIONID=ac5b8b6b7478'

    #3.将cookie_str字符串,转成字典
    #3.1分割字符串list
    cook_list = cook_str.split("; ")
    #3.2遍历拼接
    dict_cook = {}
    for cook in cook_list:
        # print(cook, type(cook))
        dict_cook[cook.split('=')[0]] = cook.split('=')[1]
        # print(dict_cook,type(dict_cook))

    #列表推倒式
    dict_two_cook = {i.split("=")[0] : i.split("=")[1] for i in cook_str.split("; ")}

    cook_dict = {
        "anonymid": "j2ugvrvr-u09ui9",
        "depovince": "BJ",
        "_r01_": "1",
        "JSESSIONID": "abcrNRGNH2FBMgrjke_rw",
        "ick_login": "7aad3f95-8ef4-4d63-b328-1bea2307db99",
        "_de": "5B6A20C030F5671D340E4CEC836F3769696BF75400CE19CC",
        "first_login_flag": "1",
        "ln_uact": "576883213@qq.com",
        "ln_hurl": "http://hdn.xnimg.cn/photos/hdn221/20121210/0935/h_main_2cyU_36ec00005b8b1375.jpg",
        "id": "501025059",
        "loginfrom": "syshome",
        "jebe_key": "4fb84a06-713b-4f42-ba8a-66598d1ced5b%7Cd9b53598af5070689701c29f5dd59698%7C1531123430038%7C1%7C1531123430208",
        "wp_fold": "0",
        "jebecookies": "571408f7-17a4-412f-91b8-d76c2448f661|||||",
        "p": "9f8d1aac3a98b126d55ad8006ec4551f9",
        "t": "29d1b5a59b00dc38b1f563479462d5fe9",
        "societyguester": "29d1b5a59b00dc38b1f563479462d5fe9",
        "xnsid": "7e35d92d",
        "XNESSESSIONID": "ac5b8b6b7478",
    }
    data = requests.get(profile_url, headers=headers, cookies=cook_dict).content.decode()
    with open("02renren2.html", 'w') as f:
        f.write(data)

if __name__ == '__main__':
    renren_profile()