#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 22-3-27 下午14：42
# @Author  : Lmq_59
import os
import time
import cv2


def make_new_folder(folder_path):
    """
    用来创建新文件夹
    :param folder_path: 文件夹的位置
    :return:
    """
    if os.path.exists(folder_path) is False:
        print(f"[INFO] 文件夹{folder_path} 不存在，正在创建……")
        os.mkdir(folder_path)
        print(f"[INFO] 文件夹{folder_path} 创建完毕。")


class Video2Picture(object):
    """
    这个类用于将视频转为图片
    """
    def __init__(self, video_path):
        """
        默认读取一个视频
        :param video_path: 视频所在路径
        """
        self.video = cv2.VideoCapture(video_path)
        self.isOpened = self.video.isOpened()
        self.video_fps = 1

    def get_video(self, video_path):
        """
        用来读取视频
        :param video_path: 视频所在路径
        :return:
        """
        self.video = cv2.VideoCapture(video_path)
        self.isOpened = self.video.isOpened()
        self.video_fps = 1

    def close_video(self):
        """
        关闭视频
        :return:
        """
        self.video.release()
        print(f"视频已关闭，如需再次加载，请使用get_video(video_path)，再次输入")

    def get_fps(self):
        """
        获取当前视频的相关信息，包括视频的FPS、总帧数以及视频时长等。
        :return:
        """
        self.video_fps = self.video.get(cv2.CAP_PROP_FPS)
        FrameNumber = self.video.get(cv2.CAP_PROP_FRAME_COUNT)
        wight = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print("[INFO] 视频FPS: {}".format(self.video_fps))
        if FrameNumber > 0:
            print("[INFO] 视频时长: {} s".format(FrameNumber/self.video_fps))
        print("[INFO] 视频是否可读: {}".format(self.isOpened))
        print("[INFO] 视频尺寸: {0}x{1}".format(wight, height))

    def get_picture(self, frame_interval, save_path, filename, form="jpg"):
        """
        开始获取图片，并保存到图片路径中，需要一定时间。
        :param frame_interval: 以多少帧的间隔读取图片
        :param save_path: 保存图片的路径
        :param filename: 保存图片的文件头，如car_0.jpg
        :param form:保存的格式，如jpg, png, jpeg等
        :return:
        """
        frame_count = 1
        count = 0
        make_new_folder(save_path)
        start_time = time.time()
        while self.isOpened:
            _, frame = self.video.read()
            if _ is False:
                break
            if frame_count % int(frame_interval) == 0:
                save_name = os.path.sep.join([save_path, "{0}_{1}.{2}".format(filename, count, form)])
                cv2.imwrite(save_name, frame)
                count += 1
                print("\t保存图片:{}".format(save_name))
            frame_count += 1
        end_time = time.time()
        print("[INFO] 总共保存：{0}张图片，共耗时{1}秒。".format(count, end_time-start_time))
        self.close_video()

    def batch_process_video(self, folder_path, save_path, picture_interval=1, picture_format='jpg'):
        """
        用于批量处理多个视频，可以提供的视频格式如下：'.avi', '.mp4', '.mpeg', '.flv'。
        默认以1帧的间隔转换所有视频，保存图片格式为jpg
        :param folder_path: 视频所在文件夹
        :param save_path: 图片保存文件夹
        :param picture_interval: 帧率间隔处理图片，默认为 1
        :param picture_format: 保存图片格式, 默认为 'jpg'
        :return:
        """
        video_format = ['.avi', '.mp4', '.mpeg', '.flv']
        VideoDictionary = {"Video": [],
                           "VideoName": [],
                           "VideoSaveName": []}
        video_lists = []
        save_path_lists = []
        files = os.listdir(folder_path)
        for file in files:
            for video_form in video_format:
                if video_form in file:
                    file_ = file.split('.')[0]
                    filename_ = os.path.sep.join([folder_path, file])
                    save_name_ = os.path.sep.join([save_path, file.split('.')[0]])
                    make_new_folder(save_name_)
                    # print(filename_)
                    # print(os.path.sep.join([folder_path, file]))
                    VideoDictionary["VideoName"].append(file_)
                    VideoDictionary["Video"].append(filename_)
                    VideoDictionary["VideoSaveName"].append(save_name_)
                    video_lists.append(filename_)
                    save_path_lists.append(save_name_)
        # print(VideoDictionary)
        for v in range(len(VideoDictionary["Video"])):
            video_name = VideoDictionary["Video"][v]
            save_path = VideoDictionary["VideoSaveName"][v]
            file = VideoDictionary["VideoName"][v]
            # print(video_name, save_path, file)
            self.get_video(video_name)
            self.get_fps()
            self.get_picture(frame_interval=picture_interval, save_path=save_path, filename=file, form=picture_format)
        print("[INFO] 批量处理完毕！")
