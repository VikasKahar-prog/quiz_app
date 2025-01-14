import customtkinter as ctk
import tkinter as tk
from PIL import Image,ImageTk
from leader import LeaderBoard
import tkinter.messagebox as msg

class PopUp(ctk.CTk):
    def __init__(self,parent_frame,add_frame,navigate_frame,newtitle):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame
        self.navigate_frame_method = navigate_frame
        self.newtitle = newtitle

        self.width = 600
        self.height = 300
        self.title(self.newtitle)
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,500,300))
        #self.config(bg="#ffbe0b")

        self.popup_frame = ctk.CTkFrame(self.parent_frame,bg_color="#ffbe0b")
        self.popup_frame.pack(fill = "both",expand = True)

        self.add_frame_method("popup",self.popup_frame)

        self.mainframe = ctk.CTkFrame(self.popup_frame,border_width=1,border_color="#ffffff",fg_color="#edede9",bg_color="#edede9")
        self.mainframe.pack(fill = "both",expand = True,anchor = "center",pady = 10,padx = 10)
        
        self.message_val = tk.StringVar()
        self.message_val.set("Congratulations")
        self.message_lbl = ctk.CTkLabel(self.mainframe,textvariable = self.message_val,fg_color="#edede9",font = ctk.CTkFont(family="Tahoma",size=30,weight="bold"))
        self.message_lbl.pack(side = "top",anchor = "center",pady = 20)

        self.score_lbl = ctk.CTkLabel(self.mainframe,text="Your Score is:",fg_color="#edede9",font = ctk.CTkFont(family="Arial",size=20,weight="normal"))
        self.score_lbl.pack(anchor = "center",pady = 10)
        
        self.score_val = tk.StringVar()
        self.score_val.set("80") 
        self.score_val = ctk.CTkLabel(self.mainframe,textvariable = self.score_val,bg_color="#ffffff",fg_color="#edede9",font = ctk.CTkFont(family="Helvetica",size=40,weight="bold"))
        self.score_val.pack(anchor = "center",pady = 5)

        home_image = ctk.CTkImage(dark_image=Image.open(r'C:\Users\lucky\OneDrive\Desktop\SYCS SEM3\QuizScienceMela\Science_Mela\pics_folder\home.png'),size = (20,20))

        self.homebutton = ctk.CTkButton(self.mainframe,corner_radius = 100,image=home_image,hover="disabled",fg_color = "#29B6F6",text = "Back to Home",text_color = "black",font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 15))
        self.homebutton.pack(side = "bottom",anchor = "center",pady = (0,20),ipadx = 10,ipady = 10)

    def go_to_home(self):
        self.navigate_frame_method("popup","homepage")

'''popmessage = PopUp()
popmessage.mainloop()'''
