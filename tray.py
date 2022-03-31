# import os
# import shutil
# import xml.etree.ElementTree as ET
# import cv2
# from numpy import zeros
#
#
# def make_new_folder(folder_path):
#     """
#     用来创建新文件夹
#     :param folder_path: 文件夹的位置
#     :return:
#     """
#     if os.path.exists(folder_path) is False:
#         print(f"[INFO] 文件夹{folder_path} 不存在，正在创建……")
#         os.mkdir(folder_path)
#         print(f"[INFO] 文件夹{folder_path} 创建完毕。")
#
#
# def change_image_brightness(image, image_path, a=0.5, g=10):
#     """
#     用来改变图片的亮度，并保存到新的文件地址
#     :param image: 输入的图片，需要opencv格式
#     :param image_path: 需要保存的文件位置
#     :param a: 亮度控制，0-1，默认为 0.5
#     :param g: 默认为 10
#     :return:
#     """
#     h, w, ch = image.shape
#     src2 = zeros([h, w, ch], image.dtype)
#     dst = cv2.addWeighted(image, a, src2, 1 - a, g)
#     cv2.imshow('dst', dst)
#     cv2.waitKey(25)
#     cv2.imwrite(image_path, dst)
#
#
# def copyh2t(file_path, new_file_path):
#
#     shutil.copy(file_path, new_file_path)
#
#
# def deal_xml(xml_path, file_name, user_path):
#     doc = ET.parse(xml_path)
#     root = doc.getroot()
#     sub1 = root.find('filename')  # 找到filename标签，
#     sub1.text = file_name
#     sub2 = root.find('path')
#     sub3 = root.find('folder')
#     sub2.text = user_path + sub3.text + '\\' + file_name
#     doc.write(xml_path)  # 保存修改
#
#
# def find_file():
#     # 从标签文件中找到对应的文件并放在新的文件夹中
#     this_path = os.getcwd()
#     xmls_path = '/new_x'
#     images_path = '/new_i'
#     new_xmls_path = '/new_xml'
#     new_images_path = '/new_images'
#     files_xml = os.listdir(this_path + xmls_path)
#     if os.path.exists('.' + new_xmls_path) == False:
#         os.makedirs('.' + new_xmls_path)
#     if os.path.exists('.' + new_images_path) == False:
#         os.makedirs('.' + new_images_path)
#     print(this_path)
#
#     for file_ in files_xml:
#         print(file_)
#         if os.path.exists('.' + new_xmls_path + '/' + file_) == False:
#             os.makedirs('.' + new_xmls_path + '/' + file_)
#         if os.path.exists('.' + new_images_path + '/' + file_) == False:
#             os.makedirs('.' + new_images_path + '/' + file_)
#         path_xml_label = this_path + xmls_path + '/' + file_
#         files_ = os.listdir(path_xml_label)
#         for file__ in files_:
#             print(file__)
#             xml_name = os.path.splitext(file__)
#             xml_path = path_xml_label + '/' + xml_name[0] + xml_name[1]
#             new_xml_path = this_path + new_xmls_path + '/' + file_ + '/' + xml_name[0] + xml_name[1]
#             image_path = this_path + images_path + '/' + file_ + '/' + xml_name[0] + '.jpg'
#             new_image_path = this_path + new_images_path + '/' + file_ + '/' + xml_name[0] + '.jpg'
#             copyh2t(image_path, new_image_path)
#             copyh2t(xml_path, new_xml_path)
#
#
# def get_new_image():
#     # 改变图片亮度，并复制粘贴标签文件
#     a = [1.3]
#     this_path = os.getcwd()
#     data_path = "\\test_data\\"
#     img_path = 'Mr_Hai_2\\'
#     xml_path = 'Mr_Hai_xmls_2\\'
#     color_name = data_path + 'new_color_'
#     x_color_name = data_path + 'new_color_xmls_'
#     files = os.listdir(this_path + data_path + img_path)
#
#     print(files)
#     for i in range(len(a)):
#         new_img_folder_path = this_path + color_name + str(i) + '_' + str(int(a[i]*10))
#         new_xml_folder_path = this_path + x_color_name + str(i) + '_' + str(int(a[i]*10))
#         make_new_folder(new_img_folder_path)
#         make_new_folder(new_xml_folder_path)
#         for step, file in enumerate(files):
#             print(step)
#             img_name_path = this_path + data_path + img_path + file
#             new_img_name_path = new_img_folder_path + "/" + file
#             # print(img_name_path, new_img_name_path)
#             img = cv2.imread(img_name_path)
#             img = cv2.resize(img, (224, 224))
#             cv2.imshow('img', img)
#             # cv2.waitKey(1)
#             change_image_brightness(img, a[i], 10, new_img_name_path)
#             now_xml_path = this_path + data_path + xml_path + file.split('.')[0] + ".xml"
#             new_xml_path = new_xml_folder_path + "/" + file.split('.')[0] + ".xml"
#             shutil.copy(now_xml_path, new_xml_path)
#
#
# # get_new_image()
#
#
# def mian():
#     # this_path = os.getcwd()
#     #
#
#     # 将文件夹中的图片进行排序
#     this_path = os.getcwd()
#     xml = '/test_data/raw_half_xmls'
#     images = '/test_data/raw_half_images'
#     path = this_path + xml
#     xml_path = path + '/'
#     images_path = this_path + images + '/'
#     user_path = "F:\\pythonProject\\TOOLS\\ForPictureAndVideo\\test_data\\raw_half_images"
#     files = os.listdir(path)
#     print(files)
#     for _, file0 in enumerate(files):
#
#         files_ = os.listdir(path + '/' + file0)
#         for i, file in enumerate(files_):
#             print(i)
#             # 获得一级目录下的所有文件
#             path0 = path + '/' + file
#             # 得到该一级文件目录文件内的绝对路径
#             ext = os.path.splitext(file)
#             new_xml_file_name = file0 + '_' + str(i) + '.xml'
#             new_img_file_name = file0 + '_' + str(i) + '.jpg'
#             img_file_path = images_path + file0 + '/'
#             img_file = ext[0] + '.jpg'
#             xml_file = xml_path + file0 + '/' + file
#             deal_xml(xml_path=xml_file, file_name=new_img_file_name, user_path=user_path)
#
#             os.chdir(xml_path + '/' + file0 + '/')
#             os.rename(file, new_xml_file_name)
#
#             os.chdir(img_file_path)
#             os.rename(img_file, new_img_file_name)
#             print(i, '----------done--------')
#
#
# # mian()
#
#
# def main():
#     # 将某文件夹中所有文件夹中的文件复制粘贴到某文件夹中
#     this_path = os.getcwd()
#     img_path = '/test_data/raw_half_images/'
#     xml_path = '/test_data/raw_half_xmls'
#     new_img_path = '/test_data/raw_3quarter_images/'
#     new_xml_path = '/test_data/raw_3quarter_xmls/'
#     files = os.listdir(this_path + xml_path)
#     for file in files:
#         files_ = os.listdir(this_path + xml_path + '/' + file)
#         for i, file_ in enumerate(files_):
#             file_name = os.path.splitext(file_)
#             make_new_folder(this_path + new_xml_path)
#             make_new_folder(this_path + new_img_path)
#             old_xml_file_path = this_path + xml_path + '/' + file + '/' + file_name[0] + file_name[1]
#             new_xml_file_path = this_path + new_xml_path + '/' + file_name[0] + file_name[1]
#             copyh2t(old_xml_file_path, new_xml_file_path)
#
#             old_img_file_path = this_path + img_path + '/' + file + '/' + file_name[0] + '.jpg'
#             new_img_file_path = this_path + new_img_path + '/' + file_name[0] + '.jpg'
#             copyh2t(old_img_file_path, new_img_file_path)
#             print(i, '----------done--------')
#
#
# main()
#
#
# def renaming():
#     this_path = os.getcwd()
#     xml = '/xml'
#     images = '/images'
#     path = this_path + xml
#     xml_path = path + '/'
#     user_path = "E:\\Pycharm\\peixun\\2\\images\\"
#     i = 0
#     files_ = os.listdir(path)
#     for file in files_:
#         # 得到该一级文件目录文件内的绝对路径
#         ext = os.path.splitext(file)
#         new_xml_file_name = str(i) + '.xml'
#         new_img_file_name = str(i) + '.jpg'
#         img_file_path = this_path + images + '/'
#         img_file = ext[0] + '.jpg'
#         xml_file = xml_path + file
#         doc = ET.parse(xml_file)
#         root = doc.getroot()
#         sub1 = root.find('filename')  # 找到filename标签，
#         sub1.text = new_img_file_name
#         sub2 = root.find('path')
#         sub3 = root.find('folder')
#         sub2.text = user_path + sub3.text + '\\' + sub1.text
#         doc.write(xml_file)  # 保存修改
#
#         os.chdir(xml_path + '/')
#         os.rename(file, new_xml_file_name)
#
#         os.chdir(img_file_path)
#         os.rename(img_file, new_img_file_name)
#         print(i, '----------done--------')
#         i += 1
#
#
# # renaming()
