"""
File Tools
"""
import os


def get_dir_files_list(path='./', recursion=False):
    """
    Collect file information from the specified directory
    :param path: Retrieve the target path for the file list
    :param recursion: Is the boolean type recursive during the process of obtaining the file list
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
