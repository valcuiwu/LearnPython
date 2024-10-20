from urllib.request import urlopen,Request
import re,os

tmp = []

page = input("要下载的页数：")
if page.isdigit():
    page = int(page)
else:
    print('请输入正确的数字！')

for i in range(2,page+2):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    url = f'http://www.netbian.com/meinv/index_{i}.htm'
    req = Request(url,headers={'User-Agent':user_agent})

    data = urlopen(req).read().decode('gbk')
    # print(data)

    link = re.findall('target="_blank"><img src="(.*?)" alt="(.*?)" />',data)

    tmp.extend(link)

# for i in link:
#     print(i)
#     jpg_url=i[0]
#     jpg_name=i[1].replace(' ','_')
#     with open(f'{jpg_name}.jpg','wb') as f:
#         f.write(urlopen(jpg_url).read())

path = os.getcwd() + '/' + 'img'
if not os.path.isdir(path):
    os.mkdir(path)
for i in tmp:
    jpg_name = i[-1].replace(' ','_').replace('*','_')
    req = Request(url=i[0],headers={'User-Agent':user_agent})
    with open('{}/{}.jpg'.format(path,jpg_name),'wb') as f:
        f.write(urlopen(req).read())
        print(jpg_name,'已下载')
input("下载完成，按回车键结束")