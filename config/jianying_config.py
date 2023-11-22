#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from configparser import ConfigParser
import os

class ReadJianyingConfigFile(object):
    def read_config(self):
        conn = ConfigParser()
        # os.path.dirname(sys.argv[0])可以获取当前项目的相对路径
        jianying_config_path = os.path.join(os.path.dirname(sys.argv[0]), 'jianying_config.ini')
        print(jianying_config_path)
        if not os.path.exists(jianying_config_path):
            raise FileNotFoundError("文件不存在")

        conn.read(jianying_config_path)
        origin_draft_path = conn.get('common','origin_draft_path')
        dest_ugc_wav_root_folder_path = conn.get('wavfile','dest_ugc_wav_root_folder_path')


        return [origin_draft_path,dest_ugc_wav_root_folder_path]

rc = ReadJianyingConfigFile()
print(rc.read_config())