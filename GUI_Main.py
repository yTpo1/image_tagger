import tkinter as tk
from DBConnection import *
from DBSelectQueries import DBSelectQueries as DS
import tkinter.messagebox


class GUI_Main(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # <create the rest of your GUI here>
        # self.configure_gui()

        self.container_1()
        self.container_dropdown()

        # button = tk.Button(root, text="OK", command=self.get_value_from_dropdown)
        # button.pack(side = tk.BOTTOM)

    def configure_gui(self):
        root.title("Image DB")
        root.geometry("700x300")

    def container_1(self):
        container_1 = tk.Frame(root, bg="blue")

        self.buttons_top(container_1)

        container_1.pack(side="top")

    def buttons_top(self, container):

        b_add_images_to_db = tk.Button(container, text="Add images to DB", command=self.choice_add_photos_to_db)
        b_add_images_to_db.pack(side=tk.LEFT, padx=2, pady=2)

        b_assign_img_to_artist = tk.Button(container, text="Assign images to artist", command=self.choice_assign_current_photos_to_artist)
        b_assign_img_to_artist.pack(side=tk.LEFT, padx=2, pady=2)

        b_assign_img_to_genre = tk.Button(container, text="Assign images to genre", command=self.choice_assign_current_photos_to_genre)
        b_assign_img_to_genre.pack(side=tk.LEFT, padx=2, pady=2)

        b_select_images_genre = tk.Button(container, text="Select images with genre", command=self.choice_get_images_of_genre)
        b_select_images_genre.pack(side=tk.LEFT, padx=2, pady=2)

        b_select_images_artist = tk.Button(container, text="Select images with artist name", command=self.choise_get_images_of_artist_name)
        b_select_images_artist.pack(side=tk.LEFT, padx=2, pady=2)

        b_img_file_extension = tk.Button(container, text="Select images with file extension", command=self.choice_get_images_of_file_extension)
        b_img_file_extension.pack(side=tk.LEFT, padx=2, pady=2)

    def choice_add_photos_to_db(self):
        print("add photos to DB")

    def choice_assign_current_photos_to_artist(self):
        print("value is:" + self.v_artist_name.get())
        print("assign_current_photos_to_artist")

    def choice_assign_current_photos_to_genre(self):
        print("value is:" + self.variable_genre.get())
        print("assign_current_photos_to_genre")

    def choice_get_images_of_genre(self):
        print("value is:" + self.variable_genre.get())
        print("get_images_of_genre")

    def choice_get_images_of_file_extension(self):
        print("value is:" + self.variable_f_exntension.get())
        print("get_images_of_file_extension")

    def choise_get_images_of_artist_name(self):
        print("value is:" + self.v_artist_name.get())
        print("get_images_of_artist_name")
        #if no such value - popup
        tk.messagebox.showinfo('Error', 'No such artist: ' + self.v_artist_name.get())

    def container_dropdown(self):
        container_2 = tk.Frame(root)
        self.drop_down_widget()

        text = tk.Label(root, text="Artist name: ")
        text.pack(side = tk.LEFT)

        self.v_artist_name = tk.StringVar(root)
        e = tk.Entry(root, textvariable=self.v_artist_name)
        e.pack(side = tk.LEFT)

        container_2.pack(side = tk.BOTTOM)

    # enter text
    def get_value_from_dropdown(self):
        print("value is:" + self.variable_genre.get())

    def drop_down_widget(self):
        # get existing genres from DB
        connection = create_connection()
        genres = DS.sql_get_all_genres(connection)
        close_connection(connection)

        genres_my = []
        for item in genres:
            genres_my.append(item['name'])

        self.variable_genre = tk.StringVar(root)
        self.variable_genre.set(genres_my[0])  # default value

        dropdown_gernres = tk.OptionMenu(root, self.variable_genre, *genres_my)
        dropdown_gernres.pack(side = tk.LEFT)

        f_exntensions = ['jpg', 'gif', 'png']
        self.variable_f_exntension = tk.StringVar(root)
        self.variable_f_exntension.set(f_exntensions[0])
        dropdown_file_extension = tk.OptionMenu(root, self.variable_f_exntension, *f_exntensions)
        dropdown_file_extension.pack(side = tk.LEFT)


if __name__ == "__main__":
    root = tk.Tk()
    GUI_Main(root).pack(side="top", fill="both", expand=True)
    root.mainloop()