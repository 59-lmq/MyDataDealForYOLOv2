# 此文件夹是用来处理图片以及视频的

## 图片处理

包括改变亮度旋转等操作，主要用于yolo系列的数据集处理

（毕竟torch自带rotation）



## 视频处理

包括录制视频、从视频中获取各帧图片、将图片按照一定帧数转换为视频等。

### VideoToPicture.py

视频转图片

Usage:
1、单个视频处理

```python 
python VideoToPicture.py --VideoPath=<your-video-path> --SavePath=<your-pic-path> --Object=<your-pic-name> --Start=True
```

Example:
    Here is a video in my folder(./data/video/capture0.avi), I want to save picture to folder(./data/picture/test0/).
    Now I write:

    ```python 
    python VideoToPicture.py -v ./data/video/capture0.avi -s ./data/picture/test0 --Start=True
    ```

2、批量视频处理

``` python 
python VideoToPicture.py --VideoPath=<your-videos-path> --SavePath=<your-picture-path> --Batch_Video=True
```

Example:
    Here are some videos in folder(./data/video/). I want to save picture to folder(./data/picture/test1/)

​	Now I write:

    ```python 
    python VideoToPicture.py -v ./data/video/ -s ./data/picture/test/ -b True
    ```

