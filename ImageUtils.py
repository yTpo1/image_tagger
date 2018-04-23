from PIL import Image
import shutil


def open_image_with_url(location):
    img = Image.open(location)
    img.show()


def open_image(filename):
    location = r"C:\Users\Toshiba\Videos\Cyberpunk all" + "\\" + filename
    img = Image.open(location)
    img.show()


def copy_image(filename):
    location_file = r"C:\Users\Toshiba\Videos\Cyberpunk all" + "\\" + filename
    # destination_directory
    dst_dir = r"C:\Users\Toshiba\Videos\images_queried"
    shutil.copy(location_file, dst_dir)
