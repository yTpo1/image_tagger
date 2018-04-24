from tkinter import *
from PIL import ImageTk, Image
from FileUtils import create_img_small, delete_file, check_if_file_exists


class GUI_Static_Stuff:

    @staticmethod
    def create_window():
        window = Tk()
        return window

    @staticmethod
    def display_image(window, img_dir):
        tmp_file_path_name = "temp_images/img_small.ppm"

        if check_if_file_exists(tmp_file_path_name):
            delete_file(tmp_file_path_name)

        # resize image so it would not take all of the screen
        create_img_small(tmp_file_path_name, img_dir)

        # display the image
        image = ImageTk.PhotoImage(Image.open(tmp_file_path_name))
        panel = Label(window, image=image)
        panel.pack(side="bottom", fill = "both", expand="yes")


