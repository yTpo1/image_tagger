from DBItemAdder import DBItemAdder
from ImageDBManipulator import *
import tkinter as tk
from FileUtils import create_img_small
from PIL import ImageTk, Image
from GUI_Main import GUI_Main

# TODO: get - GUI buttons for each genre, when clicked copyes files to folder
# TODO: assign - all photos in folder, assign to a genre
if __name__ == "__main__":
    
    choice = 2
    ImgMan = ImageManipulator()

    # Select images
    if choice == 1:
        ImgMan.get_images_of_genre(2)
    # assign images to genre
    elif choice == 2:
        ImgMan.assign_current_photos_to_genre(5)
    # add images to DB
    elif choice == 3:
        ImgMan.add_photos_to_db()
    # add images to DB and assign them to a genre
    elif choice == 4:
        ImgMan.add_photos_assign_artist_and_genre_to_db("architecture")


    # GUI
    # root = tk.Tk()
    # GUI_Main(root).pack(side="top", fill="both", expand=True)
    # root.mainloop()


# TODO: when calling sql_get_photo_id() - if doesn't find anything, returns none