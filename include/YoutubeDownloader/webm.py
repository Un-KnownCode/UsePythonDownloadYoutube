import pytube
import sys
import time
import gc


def downloadwebm(url):
    webm = pytube.YouTube(url)
    print('以下输出音频质量Itag：')
    for stream in webm.streams:
        if "webm" in str(stream) and "audio" in str(stream):
            print(stream)
    webmItag = (int(input('请输入你想要下载的音频质量Itag：')))
    print("Downloading...")
    stream = webm.streams.get_by_itag(webmItag)
    judgment = int(input('是否需要更改下载下来的音频名字'
                         '(默认名字=标题名.webm 1 = 更改，2 = 不更改)：'))
    if judgment == 1:
        stream.download(filename=str(input('请输入你想要下载下来的音频名字：')),
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
