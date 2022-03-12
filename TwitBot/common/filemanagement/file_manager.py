import os
import shutil
import random


def count_files_in_dir(path):
    return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])


def copy_and_rename_files(src_path, des_path):
    for i in range(0, count_files_in_dir(src_path)):
        if not os.listdir(src_path)[i].startswith('.'):
            final_path = os.path.join(des_path, str(i) + get_file_extension(os.listdir(src_path)[i]))
            shutil.copy(os.path.join(src_path, os.listdir(src_path)[i]), final_path)


def get_file_extension(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    return file_extension


def move_and_rename_file(src_path, des_path):
    shutil.move(src_path, des_path)


def get_random_file_name(dir_path):
    random_file_no = random.randint(0, count_files_in_dir(dir_path) - 1)
    return os.listdir(dir_path)[random_file_no]
