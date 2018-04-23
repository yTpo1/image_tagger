from PIL import Image


def open_image_with_url(location):
    img = Image.open(location)
    img.show()

def open_image(filename):
    location = r"C:\Users\Toshiba\Videos\Cyberpunk all" + "\\" + filename
    img = Image.open(location)
    img.show()

    