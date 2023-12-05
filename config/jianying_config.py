#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from configparser import ConfigParser
import os

jianying_bu_config_dict = {}

# 项目名文件夹在同一层级里需要过滤的fd
jianying_draft_fd_name_filter_list = ['template.json.bak', '.DS_Store', 'template.json',
                                      'template.tmp', 'template-2.tmp', 'root_meta_info.json', '.recycle_bin']


# 获取剪影配置文件路径
def get_jianying_config_path():
    # os.path.dirname(sys.argv[0])可以获取项目当前文件夹的相对路径
    jianying_config_path = os.path.join(os.path.dirname(sys.argv[0]), 'config/jianying_config.ini')
    return jianying_config_path


def get_jianying_bu_config_conn(jianying_config_path):
    conn = ConfigParser()
    if not os.path.exists(jianying_config_path):
        raise FileNotFoundError('文件不存在')
    conn.read(jianying_config_path)
    return conn


# 初始化配置文件
def init_jianying_bu_config():
    jianying_config_path = get_jianying_config_path()
    conn = get_jianying_bu_config_conn(jianying_config_path)
    origin_draft_path = conn.get('common', 'origin_draft_path')
    jianying_bu_config_dict['origin_draft_path'] = origin_draft_path

    for key, value in conn.items('wavfile'):
        jianying_bu_config_dict[key] = value


# 获取配置项的值
def get_jianying_bu_config(key):
    if key in jianying_bu_config_dict:
        return jianying_bu_config_dict[key]
    return None


# 写入配置项的值
def set_jianying_bu_config(key, value):
    if key in jianying_bu_config_dict:
        jianying_bu_config_dict[key] = value
        return True
    raise KeyError('not exists key %s in jianying_bu_config dict' % key)


# 存储配置文件中配置项的值
def store_jianying_bu_config(section, key, value):
    jianying_config_path = get_jianying_config_path()
    conn = get_jianying_bu_config_conn(jianying_config_path)
    if type(value) != str:
        value = str(value)
    conn.set(section, key, value)
    with open(jianying_config_path, 'w') as config_file:
        conn.write(config_file)
    jianying_bu_config_dict[key] = value
    return True
