# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from config import jianying_config
from wavfile import ugc_wav_tool

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    jianying_config.init_jianying_bu_config()
    full_wav_file_sync_state = jianying_config.get_jianying_bu_config('full_wav_file_sync_state')
    if full_wav_file_sync_state == 0:
        # ugc_wav_tool.transfer_jianying_ugc_wav_file()
        jianying_config.set_jianying_bu_config('full_wav_file_sync_state', 1)
        jianying_config.update_jianying_bu_config('wavfile', 'full_wav_file_sync_state', '1')
    print('watch dog')



