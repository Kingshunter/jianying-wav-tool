#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil


# 拷贝并重命名原文件到目标文件夹中
def copy_origin_file_to_dest_folder(current_time_in_mills, origin_file_path, dest_folder_path):
    origin_file_base_name = os.path.splitext(origin_file_path)[1]
    dest_file_path = dest_folder_path + "/" + str(current_time_in_mills) + origin_file_base_name
    shutil.copy(origin_file_path, dest_file_path)
