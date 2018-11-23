from requests_html import HTMLSession
import requests
import time

url='https://www.mzitu.com/xinggan/'
def gethed(referers):
    hed={
           
    }
    return hed

def funurl(url):
    session = HTMLSession()
    re = session.get(url)
    return re
# 下载图片
def save_img(img_url,aurl):
    request = requests.get(img_url,headers=gethed(aurl))
    title = int(round(time.time()*1000))
    with open(r'python\defFun\img\%d.jpg'%title,'wb') as file:
        file.write(request.content)

re = funurl(url)
bigpageurl=re.html.find('#pins',first=True).absolute_links
bigpageurlsize =re.html.xpath('//a[@class="page-numbers"][last()]/text()')
listurl=[]
for item in bigpageurl:
    for num in range(1,int(bigpageurlsize[0])):
        listurl.append(item+str.format("/page/{}/",num))

listimgurl=[]
for itemurl in listurl:
    bigre = funurl(itemurl)
    midpageurlsize =bigre.html.xpath('//div[@class="pagenavi"]//a[last()-1]//text()')
    listurlimg=[]
    for num in range(1,int(midpageurlsize[0])):
        listurlimg.append(str(itemurl)[0:str(itemurl).index('/page')]+"/"+str(num))
   
    for target_list in listurlimg:
        imgre = funurl(target_list)
        imgurl = imgre.html.xpath('//div[@class="main-image"]//img//@src')
        aurl = imgre.html.xpath('//div[@class="main-image"]//a//@href')
        save_img(imgurl,aurl)
        listimgurl.append(imgurl,aurl)
print(listimgurl.count)



print("下载成功")