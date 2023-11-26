# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
from config import jianying_config
from wavfile import ugc_wav_tool

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jianying_config.init_jianying_bu_config()
    full_wav_file_sync_state = jianying_config.get_jianying_bu_config('full_wav_file_sync_state')
    if full_wav_file_sync_state == 0:
        print('如果是第一次使用的话，会对所有的项目做一次初始化同步')
        ugc_wav_tool.transfer_full_jianying_ugc_wav_file()
        jianying_config.set_jianying_bu_config('full_wav_file_sync_state', 1)
        jianying_config.update_jianying_bu_config('wavfile', 'full_wav_file_sync_state', '1')
        print('初始化同步已完成')
    else:
        print('是否需要进行指定文件夹的同步?如果进行指定文件夹同步，只会同步目标文件夹里生成时间最晚的一个文件后源文件夹新生成的文件')
        print('1----------------------->需要')
        print('2----------------------->不需要')
        print('请输入选择:', end='')
        choice_folder_sync_state = input()
        if choice_folder_sync_state == '1':
            print('请输入需要同步的项目名:', end='')
            sync_project_name = input()
            print(sync_project_name)
            print('指定文件夹的同步')

        elif choice_folder_sync_state == '2':
            print('不需要进行指定文件夹的同步')
