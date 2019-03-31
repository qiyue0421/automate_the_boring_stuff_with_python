import bs4
import requests
import os
import threading

# 保存在当前目录
os.makedirs('xkcd', exist_ok=True)


def downloadComic(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        print('Downloading page http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%s' % urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        comicElem = soup.select('#comic img')
        # print(comicElem)
        if not comicElem:
            print('Could not find ang comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            # 下载页面
            print('Downloading image %s...' % comicUrl)
            res = requests.get(comicUrl)
            res.raise_for_status()

            # 保存漫画
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


downloadThreads = []
# 开启14个线程
for i in range(0, 1400, 10):
    downloadThread = threading.Thread(target=downloadComic, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# 遍历每个线程，等待所有线程的join()调用返回后才继续执行主程序
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')
