from lxml import etree

# url = "https://www.bilibili.com"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
# }
# r = requests.get(url, headers=headers)
# r.encoding="urf-8"


html = etree.parse("G:\code\python\爬虫\xpth\blibli.html", etree.HTMLParser())
text = html.xpath('//ul[@class="nav-menu"]/li[@class="home"]//div/text()')
print(text)
