from DBItemAdder import DBItemAdder
from ImageDBManipulator import *
import tkinter as tk
from FileUtils import create_img_small
from PIL import ImageTk, Image
from GUI_Main import GUI_Main

# TODO: get - GUI buttons for each genre, when clicked copyes files to folder
# TODO: assign - all photos in folder, assign to a genre
if __name__ == "__main__":
    
    # choise = 1
    # ImgBoss = ImageManipulator()
    #
    # if choise == 1:
    #     ImgBoss.get_images_of_genre(9)
    # elif choise == 2:
    #     ImgBoss.assign_current_photos_to_genre(23)

    root = tk.Tk()
    GUI_Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


# TODO: when calling sql_get_photo_id() - if doesn't find anything, returns none