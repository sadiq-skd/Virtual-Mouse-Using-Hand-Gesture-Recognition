import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox,font,Tk
from PIL import ImageTk, Image
import os
try:
    root = tk.Tk() # create root window
    root.iconbitmap("./Assets/mouse_5FO_icon.ico")
    root.geometry('600x400')
    root.resizable(False,False)
    root.title("Virtual Mouse")
    root.config(bg="#00994d")
    def show_me(root):
        choice = messagebox.askyesno("Yes or No ?", "Do You Really Want To Exit?")
        if choice:
            root.destroy()
    def Start_me():
        os.system('python ./Assets/main.py')
    button_font = font.Font(size=14)
    text_label = Label(root, text="Virtual Mouse Using Hand Gesture Recognition", font=("Comic Sans MS", 19),fg='#cfcf13', bg=root.cget('bg'))
    text_label.pack(pady=10)
    logo_image = Image.open("./Assets/logo.png")  # Replace "logo.png" with the path to your logo image
    logo_image = logo_image.resize((200, 200))  # Adjust the size as needed
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = Label(root, image=logo_photo)
    logo_label.pack(pady=10)
    button_image = Image.open("./Assets/start.png")
    button_image = button_image.resize((50, 50), Image.ANTIALIAS)
    rounded_button = ImageTk.PhotoImage(button_image)
    start_button = Button(root,image=rounded_button,font=button_font, command=lambda:Start_me(),bd=5, width=60, height=50)
    start_button.place(x=40, y=290)
    button_image_stop = Image.open("./Assets/stop.png")
    button_image_stop = button_image_stop.resize((50, 50), Image.ANTIALIAS)
    rounded_button_stop = ImageTk.PhotoImage(button_image_stop)
    stop_button = Button(root,image=rounded_button_stop,font=button_font, width=60, height=50,bd=5, command=lambda: show_me(root))
    stop_button.place(x=490, y=285)
    root.mainloop()
except KeyboardInterrupt:
    sys.exit()