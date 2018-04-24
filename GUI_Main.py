import tkinter as tk
from PIL import ImageTk, Image
from FileUtils import create_img_small, delete_file, check_if_file_exists


class GUI_Main(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # my GUI stuff goes here
        w = 400
        h = 400
        parent.minsize(width=w, height=h)
        # parent.maxsize(width=w, height=h)

        self.tmp_file_path_name = "temp_images/img_small.ppm"
        img_dir = r"C:\Users\Toshiba\Videos\New folder (2)\1520220146889.jpg"

        if check_if_file_exists(self.tmp_file_path_name):
            delete_file(self.tmp_file_path_name)

        # resize image so it would not take all of the screen
        create_img_small(self.tmp_file_path_name, img_dir)

        # Image
        self.image = ImageTk.PhotoImage(Image.open("temp_images/img_default.ppm"))
        self.label2 = tk.Label(self.parent, image=self.image)
        # self.label2.image = self.image
        self.label2.pack(side="bottom", fill="both", expand="yes")

        # Buttons
        b_next_photo = tk.Button(text="Next Photo", fg="blue", command=self.display_image)
        b_next_photo.pack(side=tk.TOP)

    def display_image(self):
        # display next the image
        image2 = ImageTk.PhotoImage(Image.open(self.tmp_file_path_name))

        self.label2.configure(image=image2)
        self.label2.image = image2

