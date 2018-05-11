from DBItemAdder import DBItemAdder
from ImageDBManipulator import *
import tkinter as tk
from FileUtils import create_img_small
from PIL import ImageTk, Image
from GUI_Main import GUI_Main

# TODO: get - GUI buttons for each genre, when clicked copyes files to folder
# TODO: assign - all photos in folder, assign to a genre
if __name__ == "__main__":
    
    choice = 4
    ImgMan = ImageManipulator()

    # Select images
    if choice == 1:
        ImgMan.get_images_of_genre(12)
        print("Selected Images of genre: ")
    # add images to DB
    elif choice == 2:
        ImgMan.add_photos_to_db()
        print("Added images to DB register")
    # assign images to artist
    elif choice == 3:
        ImgMan.assign_current_photos_to_artist("Jess Seto")
        print("Images assigned to artist: ")
    # assign images to genre
    elif choice == 4:
        ImgMan.assign_current_photos_to_genre(6)
        print("Images assigned to genre: ")
    # add images to DB and assign them to a genre
    elif choice == 5:
        ImgMan.add_photos_assign_artist_and_genre_to_db("architecture")
    elif choice == 6:
        ImgMan.get_images_of_file_extension('.gif')
        print("selected images of file extenssion: ")
    elif choice == 7:
        ImgMan.get_images_of_artist_name("Angelina Stroganova")
        print("selected images of artist: ")


    # GUI
    # root = tk.Tk()
    # GUI_Main(root).pack(side="top", fill="both", expand=True)
    # root.mainloop()


# TODO: when calling sql_get_photo_id() - if doesn't find anything, returns none