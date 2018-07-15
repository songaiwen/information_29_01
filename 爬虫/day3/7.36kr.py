import requests, re, json

def load_data_36_kr():

    #1.获取目标url
    url = 'http://36kr.com/'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    #2.发送请求请求数据
    data = requests.get(url, headers=headers).content.decode()
    #3.数据解析
    #<script>var _hmt=_hmt||[];!function(){var e=document.createElement("script");e.src="//hm.baidu.com/hm.js?
    #查看网页源代码得到以上数据,进行匹配得到<script>var props=(.*)</script>
    #但是取出的数据,不正确,取出result[0]的时候报错,后面有一个数据不是json格式
    # pattern = re.compile('<script>var props=(.*),</script>')

    # <script>var props=(.*),locationnal=
    pattern = re.compile('<script>var props=(.*),locationnal=')
    result = pattern.findall(data)


    #4.保存数据
    with open("07kr.json", 'w') as f:
        f.write(result[0])

    print(result[0])
    """
    raise JSONDecodeError("Extra data", s, end)
    json.decoder.JSONDecodeError: Extra data: line 1 column 81663 (char 81662)
    用loads校验一下,发现报上面的错误, 然后用pycharm 右下角1:1的方法进行查找错误行数
    点击1:1 然后将后面的1改成81663就能找到报错的内容
    """
    json.loads(result[0])

if __name__ == '__main__':
    load_data_36_kr()
