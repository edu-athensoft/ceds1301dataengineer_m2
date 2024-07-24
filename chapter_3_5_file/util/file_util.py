"""
File Tools
"""
import os


def get_dir_files_list(path='./', recursion=False):
    """
    采集指定目录下的文件信息
    :param path: 获取文件列表的目标路径
    :param recursion: bool类型，是否在获取文件列表过程中递归；不加这个参数，默认只会采集1.txt/2.txt
    :return:
    """
    path_list = []
    # Get all file information in the specified directory
    file_name_lists = os.listdir(path)
    for file_name in file_name_lists:
        # Join the path in the parameter with the file name generated during each traversal
        file_path = os.path.join(path, file_name)
        # Convert the above relative path to an absolute path
        abs_path = os.path.abspath(file_path)
        # If it is a normal file, directly append the file path to the path_list list
        if os.path.isfile(abs_path):
            path_list.append(abs_path)
        else:
            # If the file path is a folder,
            # determine whether the recursion parameter is True and recursively call get_dir_files_list
            if recursion:
                sub_path_list = get_dir_files_list(abs_path, True)
                path_list += sub_path_list

    return path_list


# 3、封装第二个函数，用于获取还未采集的文件信息
def get_new_by_compare_lists(processed_list, all_list):
    """
    Get all the unprocessed file path information in the file path
    :param processed_list: List of processed file paths
    :param all_list: List of all file paths
    :return: List of unprocessed file paths
    """
    new_list = []
    # Loop through all the file lists
    for file_path in all_list:
        # Compare with the list of files that have been processed.
        # If the file has not been processed, add it to the new file directory.
        if file_path.replace('\\', '/') not in processed_list:
            new_list.append(file_path)

    return new_list
