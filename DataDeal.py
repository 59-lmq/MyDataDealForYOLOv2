import os
import time
import shutil
import xml.etree.ElementTree as ET
import cv2
from numpy import zeros


def make_new_folder(folder_path):
    """
    用来创建新文件夹
    :param folder_path: 文件夹的位置
    :return: bool
    """
    if not os.path.exists(folder_path):
        print(f"[INFO] 文件夹{folder_path} 不存在，正在创建……")
        os.mkdir(folder_path)
        print(f"[INFO] 文件夹{folder_path} 创建完毕。")
        return True
    return False


def change_image_brightness(image_path, new_image_path, a=0.5, g=10):
    """
    用来改变图片的亮度，并保存到新的文件地址
    :param image_path: 输入的图片路径
    :param new_image_path: 需要保存的文件位置
    :param a: 亮度控制，0-1，默认为 0.5
    :param g: 默认为 10
    :return:
    """
    image = cv2.imread(image_path)
    h, w, ch = image.shape
    src2 = zeros([h, w, ch], image.dtype)
    dst = cv2.addWeighted(image, a, src2, 1 - a, g)
    cv2.imshow('img', image)
    cv2.imshow('dst_{}'.format(a), dst)
    cv2.waitKey(1)
    cv2.imwrite(new_image_path, dst)


def rename_file(file_abs_path, file_name, new_file_name):
    """
    通过os库重命名单个文件，首先得到该文件的绝对路径下，然后进行更改名字
    :param file_abs_path: 文件所在绝对路径
    :param file_name: 当前文件名
    :param new_file_name:将要修改的文件名
    :return:
    """
    os.chdir(file_abs_path)
    os.rename(file_name, new_file_name)


def rename_files(files_abs_path, files_name: list, new_files_name: list):
    """
    通过os库重命名某个文件夹下的多个文件，首先得到该文件夹的绝对路径下，然后进行更改名字
    :param files_abs_path: 文件夹所在绝对路径
    :param files_name: 当前需要修改的所有文件名列表，如 files_name=['1.jpg', '2.txt']。
    :param new_files_name:修改后的对应文件名列表，如new_files_name=['10.jpg', 'readme.txt']
    :return:
    """
    if make_new_folder(files_abs_path):
        print("[ERROR] 当前文件夹为空，无法进行批量重命名！")
        return False
    if len(files_name) != len(new_files_name):
        print("[ERROR] 请输入相同长度的文件名列表")
        return False
    os.chdir(files_abs_path)
    for file_name, new_file_name in files_name, new_files_name:
        print(file_name, new_file_name)
        os.rename(file_name, new_file_name)
    print("[INFO] 重命名完成")
    return True


def copyh2t(file_path, new_file_path):
    """
    将文件从当前路径复制到另一个文件路径
    :param file_path: 目前文件所在绝对路径
    :param new_file_path: 将要去的文件绝对路径
    :return:
    """
    # make_new_folder(new_file_path)
    shutil.copy(file_path, new_file_path)


def deal_xml(xml_path, folder_name, file_name, user_path):
    """
    处理数据集xml文件内的<filename> <path>等
    :param xml_path: 所在xml的文件路径
    :param folder_name: 要修改的文件夹名称，指的是xml文件内<folder></folder>
    :param file_name: 要修改的文件名，指的是xml文件内<filename></filename>
    :param user_path: 要修改的文件路径，指的是xml文件内<path></path>
    :return:
    """
    doc = ET.parse(xml_path)      # 读取xml文件
    root = doc.getroot()
    sub0 = root.find('folder')
    sub0.text = folder_name
    sub1 = root.find('filename')  # 找到filename标签，
    sub1.text = file_name
    sub2 = root.find('path')
    sub2.text = user_path
    doc.write(xml_path)  # 保存修改


def rename_(origin_img_path, origin_xml_path, new_img_path, new_xml_path):
    # # 先转移，后改名
    # now_path = os.getcwd()  # 当前文件工作路径
    #
    # # 与本文件同一路径的数据
    # my_now_img_path = now_path + "/test_data2/datasets_Hai/raw_img"
    # my_now_xml_path = now_path + "/test_data2/datasets_Hai/raw_xml"
    # # 与本文件同一路径的数据，将要保存的文件夹位置
    # my_new_img_path = now_path + "/test_data2/datasets_Hai/raw_img_half"
    # my_new_xml_path = now_path + "/test_data2/datasets_Hai/raw_xml_half"
    my_now_img_path = origin_img_path
    my_now_xml_path = origin_xml_path

    my_new_img_path = new_img_path
    my_new_xml_path = new_xml_path
    make_new_folder(my_new_img_path)
    make_new_folder(my_new_xml_path)

    for folder in os.listdir(my_now_img_path):
        abs_img_path = my_now_img_path + "\\" + folder  # 未更改的图片文件夹路径
        abs_xml_path = my_now_xml_path + "\\" + folder  # 未更改的xml文件夹路径

        new_img_abs_path = my_new_img_path + "\\" + folder  # 转移后的图片文件夹路径
        new_xml_abs_path = my_new_xml_path + "\\" + folder  # 转移后的xml文件夹路径
        make_new_folder(new_img_abs_path)
        make_new_folder(new_xml_abs_path)

        for count, file in enumerate(os.listdir(abs_img_path)):
            now_img_path = abs_img_path + "\\" + file                  # 现在图片文件路径
            now_xml_path = abs_xml_path + "\\" + file.split(".")[0] + ".xml"  # 现在xml文件路径

            new_img_path = new_img_abs_path + "\\" + file                  # 转移后的图片路径
            new_xml_path = new_xml_abs_path + "\\" + file.split(".")[0] + ".xml"  # 转移后的xml文件路径

            # 1、先转移
            copyh2t(file_path=now_img_path, new_file_path=new_img_path)
            copyh2t(file_path=now_xml_path, new_file_path=new_xml_path)

            # 2、后改名
            new_img_name = new_img_abs_path + "\\" + folder + "_" + str(count) + '.jpg'
            new_xml_name = new_xml_abs_path + "\\" + folder + "_" + str(count) + '.xml'
            rename_file(file_abs_path=new_img_abs_path, file_name=new_img_path, new_file_name=new_img_name)
            rename_file(file_abs_path=new_xml_abs_path, file_name=new_xml_path, new_file_name=new_xml_name)

            xml_filename = folder + "_" + str(count) + '.jpg'
            deal_xml(xml_path=new_xml_name, folder_name=folder, file_name=xml_filename, user_path=new_img_name)
            if int(count) > 90:
                if (int(count) + 1) % 100 == 0:
                    print("[INFO] {} 转移改名完成".format(folder + "_" + str(count)))


def get_my_new_image(now_image_path, now_xml_path, new_image_path, new_xml_path):
    """
    用来批量获取多亮度的图片，并且保存
    :param now_image_path: 原始图片文件夹的绝对路径
    :param now_xml_path: 原始xml文件夹的绝对路径
    :param new_image_path: 保存的图片文件夹的绝对路径
    :param new_xml_path: 保存的xml文件夹的绝对路径
    :return:
    """

    param_a = [0.5, 0.8, 1, 1.1]   # 亮度参数
    make_new_folder(new_image_path)  # 创建文件夹
    make_new_folder(new_xml_path)

    # 获取图片文件夹中的文件夹名
    folder_name = os.listdir(now_image_path)

    for folder in folder_name:
        # 读取当前文件夹的所有图片
        files = os.listdir(now_image_path + "\\" + folder)
        for i in range(len(param_a)):

            # 创建需要保存的图片文件夹和xml文件夹
            my_new_image_path = new_image_path + "\\" + folder + "\\"
            my_new_xmls_path = new_xml_path + "\\" + folder + "\\"
            make_new_folder(my_new_image_path)
            make_new_folder(my_new_xmls_path)

            # 开始迭代循环读取图片
            for step, file in enumerate(files):
                img_path = now_image_path + "\\" + folder + "\\" + file  # 现在图片的位置
                # 将要保存的图片的位置
                new_img_path = my_new_image_path + file.split(".")[0] + "_" + str(int(param_a[i]*10)) + ".jpg"
                # 开始增加图片
                change_image_brightness(img_path, new_img_path, param_a[i], 10)

                xml_path = now_xml_path + "\\" + folder + "\\" + file.split(".")[0] + ".xml"  # 当前xml的位置
                # 将要保存的xml的位置
                new_xmls_path = my_new_xmls_path + file.split(".")[0] + "_" + str(int(param_a[i]*10)) + ".xml"
                # 从原位置复制到要保存的位置
                copyh2t(xml_path, new_xmls_path)
                # 更新xml的内容
                xml_filename = file.split(".")[0] + "_" + str(int(param_a[i]*10)) + ".jpg"
                deal_xml(xml_path=new_xmls_path, folder_name=folder, file_name=xml_filename, user_path=new_img_path)
                if int(step) > 90:
                    if (int(step) + 1) % 100 == 0:
                        print("[INFO]  增加图片成功, 图片名：{}".format(xml_filename))


def FromHereToThere(origin_img_path, origin_xml_path, new_img_path, new_xml_path, new_img_folder):

    make_new_folder(new_img_path)  # 创建文件夹
    make_new_folder(new_xml_path)

    # 获取图片文件夹中的文件夹名
    folder_name = os.listdir(origin_img_path)

    for folder in folder_name:
        # 读取当前文件夹的所有图片
        files = os.listdir(origin_img_path + "\\" + folder)

        # 开始迭代循环读取图片
        for step, file in enumerate(files):
            img_path = origin_img_path + "\\" + folder + "\\" + file  # 现在图片的位置
            # 将要保存的图片的位置
            new_image_path = new_img_path + "\\" + file
            copyh2t(img_path, new_image_path)

            xml_path = origin_xml_path + "\\" + folder + "\\" + file.split(".")[0] + ".xml"  # 当前xml的位置
            # 将要保存的xml的位置
            new_xmls_path = new_xml_path + "\\" + file.split(".")[0] + ".xml"
            # 从原位置复制到要保存的位置
            copyh2t(xml_path, new_xmls_path)
            # 更新xml的内容
            deal_xml(xml_path=new_xmls_path, folder_name=new_img_folder, file_name=file, user_path=new_image_path)
            if int(step) > 90:
                if (int(step) + 1) % 100 == 0:
                    print("[INFO]  {}转移成功".format(file.split(".")[0]))


"""
1. 首先，先对图像做亮度处理，处理完毕后，保存图像和对应的xml文件到 raw_half_images & raw_half_xmls中
3. 最后，将 raw_half_images & raw_half_xmls 中的所有文件夹的复制到 <final_images> & <final_xmls> 中
"""

if __name__ == "__main__":
    start_time = time.time()
    now_path = os.getcwd()  # 当前文件工作路径
    img_p = "/cyl/datasets/train_img"
    xml_p = "/cyl/datasets/train_ann"
    # 1、先改名
    first_img_path = now_path + img_p
    first_xml_path = now_path + xml_p

    second_img_path = now_path + img_p + "_second"
    second_xml_path = now_path + xml_p + "_second"

    rename_(origin_img_path=first_img_path, origin_xml_path=first_xml_path,
            new_img_path=second_img_path, new_xml_path=second_xml_path)

    # 2、增加图片改变亮度
    third_img_path = now_path + img_p + "_third"
    third_xml_path = now_path + xml_p + "_third"

    get_my_new_image(now_image_path=second_img_path, now_xml_path=second_xml_path,
                     new_image_path=third_img_path, new_xml_path=third_xml_path)

    # 3、将更改后的图片放到同一个文件夹下
    fourth_img_path = now_path + img_p + "_fourth"
    fourth_xml_path = now_path + xml_p + "_fourth"
    img_folder = "train_img_fourth"
    FromHereToThere(origin_img_path=third_img_path, origin_xml_path=third_xml_path,
                    new_img_path=fourth_img_path, new_xml_path=fourth_xml_path, new_img_folder=img_folder)

    end_time = time.time()
    print('use time:{}'.format(end_time - start_time))
