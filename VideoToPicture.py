#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 22-3-27 下午14：42
# @Author  : Lmq_59

import argparse
from utils import ForCV2
"""
视频转图片
Usage:
1、单个视频处理
python VideoToPicture.py --VideoPath=<your-video-path> --SavePath=<your-pic-path> --Object=<your-pic-name> --Start=True
Example:
    Here is a video in my folder(./data/video/capture0.avi), I want to save picture to folder(./data/picture/test0/).
    Now I write:
    python VideoToPicture.py -v ./data/video/capture0.avi -s ./data/picture/test0 --Start=True

2、批量视频处理
python VideoToPicture.py --VideoPath=<your-videos-path> --SavePath=<your-picture-path> --Batch_Video=True

Example:
    Here are some videos in folder(./data/video/). I want to save picture to folder(./data/picture/test1/)
    Now I write:
    python VideoToPicture.py -v ./data/video/ -s ./data/picture/test/ -b True
"""

ap = argparse.ArgumentParser(description="This is a tool for getting picture from video")
ap.add_argument("-v", "--VideoPath",
                default="./data/video/capture0.avi",
                help="path of input video，example: ./capture0.avi, 视频所在路径。或批量处理的路径：./video")
ap.add_argument("-s", "--SavePath",
                default="./data/picture/test",
                help="path of output frames，example: ./picture/ ，保存图片的路径")
ap.add_argument("-o", "--ObjectName",
                default="Object",
                help="Name of Object，example: car or None，单个视频过程中图片保存的名字")
ap.add_argument("-fi", "--frame_interval",
                default=1,
                help="for save interval, example: frame_interval=1 means that using 1 fps to save picture")
ap.add_argument("-st", "--Start",
                default=False,
                help="control whether to save picture, default=True，是否开启转换，默认是处理单个视频，如需处理多个视频，use --Batch_Video")
ap.add_argument("--form",
                default="jpg",
                help="choose which picture format you want. Example: png、jpeg、jpg and so on")
ap.add_argument("-b", "--Batch_Video",
                default=False,
                help="control whether open batch progress video, default=False, " +
                     "是否开启批量处理图片。请将需要的图片放置在一个文件夹中，并在 --VideoPath中输入该路径")


if __name__ == "__main__":
    args = vars(ap.parse_args())
    my_video_name = args["VideoPath"]
    my_picture_save_path = args["SavePath"]
    my_frame_interval = args["frame_interval"]
    my_filename = args["ObjectName"]
    flag = args["Start"]
    flag_batch = args["Batch_Video"]
    my_format = args["form"]
    # print(args)

    vp = ForCV2.Video2Picture(my_video_name)
    if flag:
        vp.get_fps()
        vp.get_picture(frame_interval=my_frame_interval, save_path=my_picture_save_path, filename=my_filename)
    elif flag_batch:
        vp.batch_process_video(folder_path=my_video_name, save_path=my_picture_save_path,
                               picture_interval=my_frame_interval, picture_format=my_format)
