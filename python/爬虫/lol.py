import json
import os

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.7 Mobile Safari/537.36'}
num = 1

def get_headers():
    '''
    得到json对象
    '''
   
    url = 'http://lol.qq.com/biz/hero/champion.js'

    request = requests.get(url,headers =headers)

    jsontext = request.text[request.text.find('key')-2:-1]      # 得到标准的json字符串

    jsons = json.loads(jsontext)                                # 得到python对象
    return jsons

'''
循坏组合成得到图片url
'''
def get_imgurl(jsons):
    for valu in jsons.get('keys').values():
        hero_url = 'http://lol.qq.com/biz/hero/'+valu+'.js' # 得到英雄的详资源定位符

        request = requests.get(hero_url,headers =headers)

        jsontext = request.text[request.text.find('data')-2:-1]      # 得到标准的json字符串

        jsons = json.loads(jsontext)                                # 得到python对象

        # 根据英雄创建一个文件夹
        filepaths = os.getcwd()+r'\comert\imgs\%s'%jsons.get('data').get('title')
        if not os.path.exists(filepaths):
            os.mkdir(filepaths)
        for item in jsons.get('data').get('skins'):
            yield {
                'imgid':item.get('id'),
                'num': item.get('num'),
                'name':item.get('name'),
                'filepaths':filepaths
            }
     

def save_img(yields):
    for item in yields:
        imgurl = r"http://ossweb-img.qq.com/images/lol/web201310/skin/big"+ str(item.get('imgid')) + ".jpg"
        request = requests.get(imgurl,headers =headers)

        print('爬取{0}英雄的皮肤中...'.format(item.get('name')))
        filename = item.get('filepaths')+"\\" + item.get('name').replace('/','1')+".jpg"
        with open(filename,'wb') as file:
            file.write(request.content)
        global num
        num += 1
    

if __name__ == '__main__':
    jsons = get_headers()
    imgurls = get_imgurl(jsons)
    save_img(imgurls)
    print('爬取完毕，共爬取{0}张英雄皮肤'.format(num))
