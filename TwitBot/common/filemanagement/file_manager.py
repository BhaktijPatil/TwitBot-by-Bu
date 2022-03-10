import os
import shutil


def count_files_in_dir(path):
    return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])


def copy_and_rename_files(src_path, des_path):
    for i in range(0, count_files_in_dir(src_path)):
        if not os.listdir(src_path)[i].startswith('.'):
            file_name, file_extension = os.path.splitext(os.listdir(src_path)[i])
            final_path = des_path + "\\" + str(i) + file_extension
            shutil.copy(src_path + "\\" + os.listdir(src_path)[i], final_path)
