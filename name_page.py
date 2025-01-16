import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from start_page import CountdownPage
from PIL import Image,ImageTk
import mysql.connector as mycon

class NamePage(ctk.CTk):
    def __init__(self,parent_frame,add_frame,navigate_frame,newtitle):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame
        self.navigate_frame_method = navigate_frame
        self.newtitle = newtitle

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,0,0))
        self.title(self.newtitle)
        #self.config(bg="#ffbe0b")
        # self.shared_name = self.name_entry.get()

        self.bind("<f>",self.toggle_fullscreen)

        self.name_frame = ctk.CTkFrame(self.parent_frame,fg_color="#ffbe0b")
        self.name_frame.pack(fill = "both",expand = True)

        self.back_image = ctk.CTkImage(light_image=Image.open(f"images/arrow.png"), dark_image=Image.open(f"images/arrow.png"), size=(16, 16))
    
        self.back_button = ctk.CTkButton(self.name_frame,corner_radius = 100,image=self.back_image,hover="disabled",fg_color = "transparent" , bg_color="transparent",text = "Back to Home",text_color = "black",font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 15), command = self.navigate_to_home)
        self.back_button.pack(side = "top",anchor = "w", pady = 10, padx = 10)

        self.add_frame_method("namepage",self.name_frame)

        self.middle_frame = ctk.CTkFrame(self.name_frame,width = 550,height = 350,fg_color="#001d3d",bg_color="#001d3d",corner_radius=20)
        self.middle_frame.pack(anchor='center',pady=150)

        self.name_label = ctk.CTkLabel(self.middle_frame,text="Name",width=150,height=50,corner_radius=15,fg_color="#ffffff",text_color="#000000",font = ctk.CTkFont(family = "Cursive",size = 20,weight = "bold"))
        self.name_label.place(x = 200,y = 60)
        
        self.name_value = tk.StringVar()
        self.name_value.set("Enter your name:")
        self.name_entry = ctk.CTkEntry(self.middle_frame,textvariable=self.name_value,height = 50,width=300,corner_radius=20,font = ctk.CTkFont(family="Helvetica",size = 20,weight="normal"))
        self.name_entry.bind("<FocusIn>",self.usr_focus_in)
        self.name_entry.bind("<FocusOut>",self.usr_focus_out)
        self.name_entry.place(x = 130,y = 150)

        self.play_img = ctk.CTkImage(dark_image=Image.open("images/play-button-arrowhead.png"),size=(30,30))

        self.play_button = ctk.CTkButton(self.middle_frame,width = 150,image=self.play_img,height=50,corner_radius=20,text="Play",text_color="#000000",fg_color="#ffbe0b",hover_color="#FFD54F",font = ctk.CTkFont(family = "Helvetica",size = 20,weight="bold"),command=self.checkUser)
        self.play_button.place(x = 200,y = 250)

    def toggle_fullscreen(self,event = None):
        self.overrideredirect(True)

    def checkUser(self):
        name = self.name_value.get()
        if name == "" or name == "Enter your name:":
            messagebox.showwarning(title="Warning",message="Please enter your name:")
        else:
            try:
                con = mycon.connect(host = "localhost", username = "root", password = "root", port = 3307, database = "quiz_app")
                cur = con.cursor()
                insert_query = "insert into leaderboard(name) values(%s)"
                insert_values = (name,)
                cur.execute(insert_query, insert_values)
                con.commit()
                print(f"{cur.rowcount} record inserted")
                con.close()
            except Exception as e:
                print("Error : ", e)

            start_page_object =  CountdownPage(self.parent_frame,self.add_frame_method,self.navigate_frame_method,"Start Page")
            self.navigate_frame_method("namepage","startpage")

    def usr_focus_in(self,event):
        if self.name_value.get() == "Enter your name:":
            self.name_entry.delete(0,ctk.END)

    def usr_focus_out(self,event):
        if self.name_value.get() == "":
            self.name_entry.insert(0,"Enter your name:")

    def navigate_to_home(self):
        self.navigate_frame_method("namepage","homepage")

