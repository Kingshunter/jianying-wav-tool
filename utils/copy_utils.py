#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import time

# 拷贝并重命名原文件到目标文件夹中
def copy_origin_file_to_dest_folder(origin_file_path, dest_folder_path):
    origin_file_base_name = os.path.splitext(origin_file_path)[1]
    current_time_in_mills = int(round(time.time() * 1000))
    dest_file_path = dest_folder_path + "/" + str(current_time_in_mills) + origin_file_base_name
    print(dest_file_path)
    shutil.copy(origin_file_path, dest_file_path)
