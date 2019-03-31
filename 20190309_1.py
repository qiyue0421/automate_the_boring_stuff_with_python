"""import webbrowser
import pyperclip

address = pyperclip.paste()
webbrowser.open('https://map.baidu.com/?newmap=1&ie=utf-8&s=s%26wd%3D' + address)
"""
"""
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('123.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
"""
import bs4
import requests
import os
import threading

url = 'http://xkcd.com'
# 保存在当前目录
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    comicElem = soup.select('#comic img')
    # print(comicElem)
    if not comicElem:
        print('Could not find ang comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # print(comicUrl)
        # 下载页面
        print('Downloading image %s...' % comicUrl)
        res = requests.get(comicUrl)
        res.raise_for_status()

        # 保存漫画
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
