import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

class NamePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,0,0))
        self.title("NamePage")
        self.config(bg="#ffbe0b")

        self.bind("<f>",self.toggle_fullscreen)

        self.middle_frame = ctk.CTkFrame(self,width = 550,height = 400,fg_color="#001d3d",bg_color="#001d3d",corner_radius=20)
        self.middle_frame.place(x = 350,y = 120)

        self.name_label = ctk.CTkLabel(self.middle_frame,text="Name",width=150,height=50,corner_radius=15,fg_color="#ffffff",text_color="#000000",font = ctk.CTkFont(family = "Cursive",size = 20,weight = "bold"))
        self.name_label.place(x = 200,y = 100)
        
        self.name_value = tk.StringVar()
        self.name_value.set("Enter your name:")
        self.name_entry = ctk.CTkEntry(self.middle_frame,textvariable=self.name_value,height = 50,width=300,corner_radius=20,font = ctk.CTkFont(family="Helvetica",size = 20,weight="normal"))
        self.name_entry.bind("<FocusIn>",self.usr_focus_in)
        self.name_entry.bind("<FocusOut>",self.usr_focus_out)
        self.name_entry.place(x = 130,y = 170)


        self.play_img = ctk.CTkImage(dark_image=Image.open("images/play-button-arrowhead.png"),size=(30,30))

        self.play_button = ctk.CTkButton(self.middle_frame,width = 150,image=self.play_img,height=50,corner_radius=20,text="Play",text_color="#000000",fg_color="#ffbe0b",hover_color="#FFD54F",font = ctk.CTkFont(family = "Helvetica",size = 20,weight="bold"),command=self.checkUser)
        self.play_button.place(x = 200,y = 270)

    def toggle_fullscreen(self,event = None):
        self.overrideredirect(True)

    def checkUser(self):
        if self.name_value.get() == "" or self.name_value.get() == "Enter your name:":
            messagebox.showwarning(title="Warning",message="Please enter your name:")

    def usr_focus_in(self,event):
        if self.name_value.get() == "Enter your name:":
            self.name_entry.delete(0,ctk.END)

    def usr_focus_out(self,event):
        if self.name_value.get() == "":
            self.name_entry.insert(0,"Enter your name:")


namepage = NamePage()
namepage.mainloop()
                      
