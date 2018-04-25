import json
import os
from PIL import Image
import shutil


def create_img_small(tmp_file_path_name, img_path_name):
    """Open an image, resize it, save it"""
    image = Image.open(img_path_name)
    image = image.resize((250,250), Image.ANTIALIAS)
    image.save(tmp_file_path_name, "ppm")


def check_if_file_exists(file_path_name):
    return os.path.exists(file_path_name)


def get_file_extension(path):
    path_split = os.path.splitext(path)
    return path_split[1]


def delete_file(file_path_name):
    os.remove(file_path_name)


def copy_image(filename):
    location_file = r"C:\Users\Toshiba\Videos\Cyberpunk all" + "\\" + filename
    # destination_directory
    dst_dir = r"C:\Users\Toshiba\Videos\images_queried"
    shutil.copy(location_file, dst_dir)


def get_file_names_from_folder(directory):
    directory_items_list = os.listdir(directory)
    return directory_items_list


def read_json_file(file):
    with open(file) as json_file:
        data = json.load(json_file)
    return data

# def open_image_with_url(location):
#     img = Image.open(location)
#     img.show()
#
#
# def open_image(filename):
#     location = r"C:\Users\Toshiba\Videos\Cyberpunk all" + "\\" + filename
#     img = Image.open(location)
#     img.show()