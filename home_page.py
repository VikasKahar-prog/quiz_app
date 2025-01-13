import customtkinter as ctk 
import tkinter as tk
from PIL import Image,ImageTk
from name_page import NamePage

class HomePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()        
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,-10,0))
        self.config(bg="#ffbe0b")

        self.title("QUIZ APP")

        self.quiz_frame = ctk.CTkFrame(self)
        
        self.bgimage = ctk.CTkImage(dark_image=Image.open(r"C://Users//vikas//Downloads//153685313_38076096-ce6c-473d-a081-481373ca1733.jpg"),size=(400, 400))
        self.bglabel = ctk.CTkLabel(self.quiz_frame,image = self.bgimage,text = "")
        self.bglabel.pack()

        self.quiz_frame.place(x = 100, y = 150)

        self.logo_frame = ctk.CTkFrame(self, fg_color="#001d3d")
        self.logo_image = ctk.CTkImage(dark_image=Image.open(r"C://Users//vikas//Downloads//Screenshot_2025-01-11_153522-removebg-preview.png"),size=(400, 100))
        self.logo_label = ctk.CTkLabel(self.logo_frame,image = self.logo_image,text = "")
        self.logo_label.pack()

        self.logo_frame.place(x = 100, y = 600)

        self.text_frame = ctk.CTkFrame(self, fg_color="#ffbe0b", bg_color="#ffbe0b")
        self.text1 = ctk.CTkLabel(self.text_frame, text="Let's play", text_color="#001d3d", font=ctk.CTkFont(family="jokerman",weight="bold", size=40))
        self.text1.pack(side = tk.LEFT)
        self.text2 = ctk.CTkLabel(self.text_frame, text="Quiz", text_color="#001d3d", font=ctk.CTkFont(family="jokerman",weight="bold", size=90))
        self.text2.pack(padx = 10, side = tk.RIGHT)
        self.text_frame.place(x = 800, y = 250)


        self.start_button = ctk.CTkButton(self, text="START", fg_color="#001d3d", text_color="white", height=45, width=200, font=ctk.CTkFont(family="Verdana Pro", size=20, weight="bold"), corner_radius=10, bg_color="#ffbe0b")
        self.start_button.place(x = 900, y = 430)

        self.leader_board_image = ctk.CTkImage(dark_image=Image.open(r"C://Users//vikas//Downloads//winner.png"), size=(100, 100))
        self.ld_board_button = ctk.CTkButton(self, text="", image=self.leader_board_image, fg_color="#ffbe0b", bg_color="#ffbe0b", hover=False, cursor = "hand2")
        self.ld_board_button.place(x = 1400, y = 30)
    
if __name__ == "__main__":
    quiz_app = HomePage()
    quiz_app.mainloop()