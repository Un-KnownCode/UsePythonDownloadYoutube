import pytube
import sys
import time
import gc


def downloadvideo(url):
    video = pytube.YouTube(url)
    print('以下输出视频质量Itag：')
    for stream in video.streams:
        if "video" in str(stream) and "mp4" in str(stream):
            print(stream)
    videoItag = (int(input('请输入你想要下载的视频质量Itag：')))
    print("Downloading...")
    stream = video.streams.get_by_itag(videoItag)
    judgment = int(input('是否需要更改下载下来的视频名字'
                         '(默认名字=标题名.mp4 1 = 更改，2 = 不更改)：'))
    if judgment == 1:
        stream.download(filename=str(input('请输入你想要下载下来的视频名字：')),
                        output_path=str(input('请输入你想要下载到的地址：')))
    if judgment == 2:
        stream.download(output_path=str(input('请输入你想要下载到的地址：')))
    else:
        print('输入错误，程序将在三秒后终结：')
        gc.collect()
        time.sleep(3)
        print('程序退出')
        sys.exit()
    print("Done")
