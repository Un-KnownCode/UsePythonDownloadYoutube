import sys
import time
import gc
from include.YoutubeDownloader import Video
from include.YoutubeDownloader import webm
from include.YoutubeDownloader import all

url = input('请输入你想要下载的Youtube地址：')

number = int(input('下载视频输入 1 ，下载音频输入 2 ，下载视频 + 音频输入 3：'))

if number == 1:
    # 下载视频
    Video.downloadvideo(url)
if number == 2:
    # 下载音频
    webm.downloadwebm(url)
if number == 3:
    # 音频视频全部下载
    all.downloadall(url)
else:
    # 若number不是1,2,3其中一个，直接退出程序
    print('输入错误，程序将在三秒后终结：')
    gc.collect()
    time.sleep(3)
    print('程序退出')
    sys.exit()
