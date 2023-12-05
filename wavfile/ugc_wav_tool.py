#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from config import jianying_config
from utils import copy_utils, platform_utils, time_utils

platform = platform_utils.get_current_platform()


def transfer_full_ugc_wav_files_to_dest_folder(ugc_project_name_wav_file_dict):
    if ugc_project_name_wav_file_dict:
        for project_name, ugc_wav_file_list in ugc_project_name_wav_file_dict.items():
            dest_ugc_wav_folder = get_dest_ugc_wav_folder(project_name)
            exists_ugc_wav_folder = cheak_dest_ugc_wav_folder(dest_ugc_wav_folder)
            if exists_ugc_wav_folder:
                continue
            else:
                os.makedirs(dest_ugc_wav_folder)
                copy_full_ugc_wav_file_list_to_dest_folder(ugc_wav_file_list, dest_ugc_wav_folder)


def transfer_ugc_wav_files_to_dest_folder(project_name, ugc_wav_file_list):
    if ugc_wav_file_list:
        dest_ugc_wav_folder = get_dest_ugc_wav_folder(project_name)
        exists_ugc_wav_folder = cheak_dest_ugc_wav_folder(dest_ugc_wav_folder)
        if not exists_ugc_wav_folder:
            os.makedirs(dest_ugc_wav_folder)
        copy_ugc_wav_file_list_to_dest_folder_by_project(project_name, ugc_wav_file_list, dest_ugc_wav_folder)


# 根据全量项目内的朗读音频文件列表拷贝音频文件到目标文件夹中
def copy_full_ugc_wav_file_list_to_dest_folder(ugc_wav_file_list, dest_ugc_wav_folder):
    for ugc_wav_file in ugc_wav_file_list:
        current_time_in_mills = time_utils.get_current_time_in_mills()
        copy_utils.copy_origin_file_to_dest_folder(current_time_in_mills, ugc_wav_file, dest_ugc_wav_folder)


# 根据指定项目内的朗读音频文件列表拷贝音频文件到目标文件夹中
def copy_ugc_wav_file_list_to_dest_folder_by_project(project_name, ugc_wav_file_list, dest_ugc_wav_folder):
    current_time_in_mills = 0
    for ugc_wav_file in ugc_wav_file_list:
        current_time_in_mills = time_utils.get_current_time_in_mills()
        copy_utils.copy_origin_file_to_dest_folder(current_time_in_mills, ugc_wav_file, dest_ugc_wav_folder)
    jianying_config.store_jianying_bu_config('wavfile', project_name, current_time_in_mills)


# 判断目标文件夹是否存在
def cheak_dest_ugc_wav_folder(dest_ugc_wav_folder_path):
    if os.path.exists(dest_ugc_wav_folder_path):
        return True
    return False


def check_ugc_project_path(ugc_project_path):
    if os.path.exists(ugc_project_path):
        return True
    raise Exception('not exists ugc_project_path %s' % ugc_project_path)


# 获取目标文件夹
def get_dest_ugc_wav_folder(project_name):
    dest_ugc_wav_root_folder_path = jianying_config.get_jianying_bu_config('dest_ugc_wav_root_folder_path')
    return dest_ugc_wav_root_folder_path + "/" + project_name + "/textReading"


# 获取用户内容文件夹并按降序排序
def get_draft_ugc_project_tup_list(draft_content_fd_list, draft_origin_path):
    """
        这里使用元组列表来保存项目名和路径映射数据
    """
    ugc_project_tup_list = []
    if draft_content_fd_list:
        for fd_name in draft_content_fd_list:
            if fd_name not in jianying_config.jianying_draft_fd_name_filter_list:
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


# 生成文本朗读的文件路径列表
def generate_ugc_wav_files_list(ugc_project_path):
    ugc_project_detail_path_list = os.listdir(ugc_project_path)
    has_text_reading = judge_text_reading_folder(ugc_project_detail_path_list)
    if has_text_reading:
        ugc_text_reading_path = ugc_project_path + "/textReading"
        ugc_text_reading_file_list = os.listdir(ugc_text_reading_path)
        ugc_wav_file_list = generate_ugc_wav_file_list(ugc_text_reading_path, ugc_text_reading_file_list)
        return ugc_wav_file_list
    return None


# 根据当前操作系统类型获取剪影的draft文件夹路径
def get_jianying_draft_origin_path():
    origin_draft_path = jianying_config.get_jianying_bu_config('origin_draft_path')
    return origin_draft_path


# 查找所有用户生成的剪影声音文件
def find_all_jianying_ugc_wav_files():
    draft_origin_path = get_jianying_draft_origin_path()
    draft_content_fd_list = os.listdir(draft_origin_path)
    ugc_project_tup_list = get_draft_ugc_project_tup_list(draft_content_fd_list, draft_origin_path)
    ugc_project_name_wav_file_dict = generate_project_name_ugc_wav_file_dict(ugc_project_tup_list)
    return ugc_project_name_wav_file_dict


# 根据项目名查找用户生成的剪影声音文件
def find_jianying_ugc_wav_files_by_project(project_name):
    draft_origin_path = get_jianying_draft_origin_path()
    ugc_project_path = os.path.join(draft_origin_path, project_name)
    check_ugc_project_path(ugc_project_path)
    ugc_wav_file_list = generate_ugc_wav_files_list(ugc_project_path)
    return ugc_wav_file_list


# 根据时间过滤出新增的ugc wav file列表
def filter_ugc_wav_file_by_last_sync_time(ugc_wav_file_list, ugc_wav_file_last_sycn_time):
    if ugc_wav_file_list:
        print('---最后一次同步的毫秒数为:' + ugc_wav_file_last_sycn_time + '---')
        print('======================================')
        for i in range(len(ugc_wav_file_list) - 1, -1, -1):
            ugc_wav_file = ugc_wav_file_list[i]
            if platform == 3:
                if os.path.basename(ugc_wav_file) == '.DS_Store':
                    ugc_wav_file_list.pop(i)
                    continue
            ugc_wav_file_mtime = time_utils.get_time_in_mills_by_time_in_seconds(os.path.getmtime(ugc_wav_file))
            if int(ugc_wav_file_last_sycn_time) > ugc_wav_file_mtime:
                ugc_wav_file_list.pop(i)


# 转移剪影里用户项目中的全量wav file
def transfer_full_jianying_ugc_wav_file():
    ugc_project_name_wav_file_dict = find_all_jianying_ugc_wav_files()
    transfer_full_ugc_wav_files_to_dest_folder(ugc_project_name_wav_file_dict)


# 转移剪影里用户项目中指定项目的wav file
def transfer_jianying_ugc_wav_file_by_project(project_name):
    ugc_wav_file_list = find_jianying_ugc_wav_files_by_project(project_name)
    ugc_wav_file_last_sycn_time = jianying_config.get_jianying_bu_config(project_name)
    if ugc_wav_file_last_sycn_time:
        filter_ugc_wav_file_by_last_sync_time(ugc_wav_file_list, ugc_wav_file_last_sycn_time)
    print('---需要同步的ugc wav files:', end='')
    print(ugc_wav_file_list, end='')
    print('---')
    transfer_ugc_wav_files_to_dest_folder(project_name, ugc_wav_file_list)
