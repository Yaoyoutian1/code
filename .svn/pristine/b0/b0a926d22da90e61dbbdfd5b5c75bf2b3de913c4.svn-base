'''
requests利用cookie登陸知乎
'''
import requests

url = "https://www.zhihu.com"
headers = {
    'cookie': '_zap=854bbfd9-688a-403b-bde3-ceb0645dd5bf; d_c0="APAmKZV1Xw6PTqwjcyMVuK1STpOgkFhrLG0=|1539704334"; q_c1=ff88dcef2b7e4284a43a876a567fe0c0|1539704342000|1539704342000; _xsrf=MnOGAB4XeBISiPqgXStedMvcIRJ1TlPt; l_n_c=1; r_cap_id="NDQxZDJmZTJjNDFlNGZiZmFkMDM0NTBhYzg5ZGFmYjg=|1540475096|14ff8c560c57137820bf85f139707de45afe4d9c"; cap_id="NjVkOGJjN2MxY2QxNDk1MDgxZWRhZTAzZjVjOTIyYTI=|1540475096|2454e5bc9e4bc53341dbb87e60e64770f522f5ae"; l_cap_id="MTZmNjhhZGNmZWFhNGYwNGE4NDAxYzAwMjQyMjE0MzU=|1540475096|7f2e2f1c81d88eb9e129efbb858af1328215639a"; n_c=1; tst=r; capsion_ticket="2|1:0|10:1540475202|14:capsion_ticket|44:MjUyOGViMzg0ODQ4NDEzY2IxYTliZDc3MzA0YzBhODY=|c14943d8cdb93deb2b4f779d5502dd1d2f6efbdd4a9aea70ef78bffa5de7bab7"; z_c0=Mi4xSG1lYUJBQUFBQUFBOENZcGxYVmZEaGNBQUFCaEFsVk5TQmVfWEFBYnNxYXItMHRLTWpaSWQ1SDA0LTNEeUJmaGZ3|1540475208|a5a42440af4119c5db07b8a789e126ec2523d4bc; tgw_l7_route=29b95235203ffc15742abb84032d7e75',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
r = requests.get(url, headers=headers)
r.encoding = "utf-8"
print(r.text)

with open("G:\code\python\py.html", "wb") as f:
    f.write(r.content)
