import json
import os


def get_file_names_from_folder(directory):
    directory_items = os.listdir(directory)
    return directory_items


def read_json_file(file):
    with open(file) as json_file:
        data = json.load(json_file)
    return data

