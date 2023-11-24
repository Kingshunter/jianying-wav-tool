#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from utils import copy_utils, platform_utils

# 项目名文件夹在同一层级里需要过滤的fd
jianying_draft_fd_name_filter_list = ['template.json.bak', '.DS_Store', 'template.json',
                                      'template.tmp', 'template-2.tmp', 'root_meta_info.json', '.recycle_bin']

# 根据系统
platform = platform_utils.get_current_platform()
if platform == 1:
    print(111)
elif platform == 2:
    print("not support linux temporary")
    raise NotImplementedError("not support linux platform temporary")
elif platform == 3:
    """
        default platform by the author
    """
    dest_ugc_wav_root_folder_path = "/Users/hunter/Documents"
else:
    raise NotImplementedError("not support other platform")

def transfer_ugc_wav_file_to_dest_folder(ugc_project_name_wav_file_dict):
    if ugc_project_name_wav_file_dict:
        for project_name, ugc_wav_file_list in ugc_project_name_wav_file_dict.items():
            print(project_name, ugc_wav_file_list)
            dest_ugc_wav_folder = get_dest_ugc_wav_folder(project_name)
            exists_ugc_wav_folder = cheak_dest_ugc_wav_folder(dest_ugc_wav_folder)
            if exists_ugc_wav_folder:
                compute_dest_ugc_wav_file_md5_dict(dest_ugc_wav_folder)
                print(222)
            else:
                os.makedirs(dest_ugc_wav_folder)
                copy_ugc_wav_file_list_to_dest_folder(ugc_wav_file_list, dest_ugc_wav_folder)

# 根据项目内的朗读音频文件列表拷贝音频文件到目标文件夹中
def copy_ugc_wav_file_list_to_dest_folder(ugc_wav_file_list, dest_ugc_wav_folder):
    for ugc_wav_file in ugc_wav_file_list:

        copy_utils.copy_origin_file_to_dest_folder(ugc_wav_file, dest_ugc_wav_folder)

# 判断目标文件夹是否存在
def cheak_dest_ugc_wav_folder(dest_ugc_wav_root_folder_path):
    if os.path.exists(dest_ugc_wav_root_folder_path):
        return True
    return False

# 获取目标文件夹
def get_dest_ugc_wav_folder(project_name):
    return dest_ugc_wav_root_folder_path + "/" + project_name + "/textReading"

# 计算目标文件夹内的音频文件md5
def compute_dest_ugc_wav_file_md5_dict(dest_ugc_wav_folder):
    dest_ugc_wav_file_md5_dict = {}
    for root, dirs, files in os.walk(dest_ugc_wav_folder):
        for file in files:
            # 复制文件
            print('aaa')
            print(file)
    print('bbbb')



# 获取用户内容文件夹并按降序排序
def get_draft_ugc_project_tup_list(draft_content_fd_list, draft_origin_path):
    """
        这里使用元组列表来保存项目名和路径映射数据
    """
    ugc_project_tup_list = []
    if draft_content_fd_list:
        for fd_name in draft_content_fd_list:
            if fd_name not in jianying_draft_fd_name_filter_list:
                ugc_project_path = os.path.join(draft_origin_path, fd_name)
                # 元组信息(project_name, ugc_project_path)
                ugc_project_tup = (fd_name, ugc_project_path)
                ugc_project_tup_list.append(ugc_project_tup)
        ugc_project_tup_list.sort(key=lambda ugc_project_tup: os.path.getmtime(ugc_project_tup[1]), reverse=True)
    return ugc_project_tup_list

# 判断是否有textReading文件夹
def judge_text_reading_folder(ugc_project_detail_path_list):
    if ugc_project_detail_path_list.__contains__('textReading'):
        return True
    return False

# 生成文本朗读的文件路径列表
def generate_ugc_wav_file_list(ugc_text_reading_path, ugc_text_reading_file_list):
    ugc_wav_file_list = []
    for ugc_text_reading_file in ugc_text_reading_file_list:
        ugc_wav_file = ugc_text_reading_path + "/" + ugc_text_reading_file
        ugc_wav_file_list.append(ugc_wav_file)
    return ugc_wav_file_list

# 生成根据项目名做分类的文本朗读的文件路径字典
def generate_project_name_ugc_wav_file_dict(ugc_project_tup_list):
    ugc_project_name_wav_file_dict = {}
    if ugc_project_tup_list:
        for project_name, ugc_project_path in ugc_project_tup_list:
            ugc_project_detail_path_list = os.listdir(ugc_project_path)
            has_text_reading = judge_text_reading_folder(ugc_project_detail_path_list)
            if has_text_reading:
                ugc_text_reading_path = ugc_project_path + "/textReading"
                ugc_text_reading_file_list = os.listdir(ugc_text_reading_path)
                ugc_wav_file_list = generate_ugc_wav_file_list(ugc_text_reading_path, ugc_text_reading_file_list)
                ugc_project_name_wav_file_dict[project_name] = ugc_wav_file_list
    return ugc_project_name_wav_file_dict


# 根据当前操作系统类型获取剪影的draft文件夹路径
def get_jianying_draft_origin_path():
    platform = platform_utils.get_current_platform()
    if platform == 1:
        print("windows path")
    elif platform == 2:
        print("not support linux temporary")
        raise NotImplementedError("not support linux platform temporary")
    elif platform == 3:
        return '/Users/hunter/Movies/JianyingPro/User Data/Projects/com.lveditor.draft'
    raise NotImplementedError("not support other platform")

def find_jianying_wav_file():
    draft_origin_path = get_jianying_draft_origin_path()
    draft_content_fd_list = os.listdir(draft_origin_path)
    ugc_project_tup_list = get_draft_ugc_project_tup_list(draft_content_fd_list, draft_origin_path)
    ugc_project_name_wav_file_dict = generate_project_name_ugc_wav_file_dict(ugc_project_tup_list)
    return ugc_project_name_wav_file_dict

# 转移剪影里用户项目中的wav file
def transfer_jianying_ugc_wav_file():
    ugc_project_name_wav_file_dict = find_jianying_wav_file()
    transfer_ugc_wav_file_to_dest_folder(ugc_project_name_wav_file_dict)


