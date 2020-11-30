import pytube
import sys
import time
import gc


def downloadall(url):
    video_list = []
    # 导入URL到pytube库解析
    video = pytube.YouTube(url)
    
    # 输出视频中可供下载的视频Itag
    print('以下是视频选择区域：')
    for stream in video.streams:
        if "video" in str(stream) and "mp4" in str(stream):
            print(stream)
    
    # 导入视频Itag进video_list
    video_list.append(int(input('请输入你想要下载的视频质量Itag：')))
    
    # 输出视频中可供下载的音频Itag
    print('以下是音频选择区域：')
    for stream in video.streams:
        if "webm" in str(stream) and "audio" in str(stream):
            print(stream)
    
    # 导入音频Itag进video_list
    video_list.append(int(input('请输入你想要下载的音频质量Itag：')))
    
    # for遍历循环下载
    i = 0
    judgment = int(input('是否需要更改下载下来的视频名字以及音频名字'
                         '(默认名字=标题名.mp4, 标题名.webm / 1 = 更改，2 = 不更改)：'))
    if judgment == 1:
        videoname = input('请输入下载的视频名字：')
        webmname = input('请输入下载的音频名字：')
        for videoItag in video_list:
            i += 1
            print("Downloading...")
            stream = video.streams.get_by_itag(videoItag)
            if i == 1:
                stream.download(filename=videoname, output_path=str(input('请输入视频保存的位置：')))
            if i == 2:
                stream.download(filename=webmname, output_path=str(input('请输入音频保存的位置：')))
            print("Done")
    if judgment == 2:
        for videoItag in video_list:
            i += 1
            print("Downloading...")
            stream = video.streams.get_by_itag(videoItag)
            if i == 1:
                stream.download(output_path=str(input('请输入视频保存的位置：')))
            if i == 2:
                stream.download(output_path=str(input('请输入音频保存的位置：')))
            print("Done")
    else:
        print('输入错误，程序将在三秒后终结：')
        gc.collect()
        time.sleep(3)
        print('程序退出')
        sys.exit()
