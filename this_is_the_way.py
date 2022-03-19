import glob
import os


def get_deep_files(path):
    """
    The function gets a path to a directory, and returns a list of all the files
    that start with "deep" in the directory.
    :param path: The path of the directory we want to extract the information from.
    :return: A list of all the files that start with "deep" in the directory.
    """
    return [os.path.basename(file) for file in glob.glob(path + "/deep*")]
