import customtkinter as ctk
import tkinter as tk
from PIL import Image,ImageTk
import tkinter.messagebox as msg

class LeaderBoard(ctk.CTk):
    def __init__(self,parent_frame,add_frame,navigate_frame,newtitle):
        super().__init__()
        self.parent_frame = parent_frame
        self.add_frame_method = add_frame
        self.navigate_frame_method = navigate_frame
        self.newtitle = newtitle

        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,-10,-5))
        self.title(self.newtitle)
        #self.config(bg="#ffbe0b")

        self.leader_frame = ctk.CTkFrame(self.parent_frame,fg_color="#ffbe0b")
        self.leader_frame.pack(fill = "both",expand = True)

        self.add_frame_method("leaderboard",self.leader_frame)

        

        self.main_frame = ctk.CTkScrollableFrame(self.leader_frame,corner_radius=20,border_width=1,border_color="#000000",fg_color="#ffffff",bg_color="#ffbe0b",scrollbar_fg_color="lightgray",scrollbar_button_hover_color="gray",orientation="vertical")
        self.main_frame.pack(fill = "both",expand = True,padx = (25,25),pady = (35,60))

        self.back_image = ctk.CTkImage(light_image=Image.open(f"images/arrow.png"), dark_image=Image.open(f"images/arrow.png"), size=(16, 16))
    
        self.back_button = ctk.CTkButton(self.main_frame,corner_radius = 100,image=self.back_image,hover="disabled",fg_color = "transparent" , bg_color="transparent",text = "Back to Home",text_color = "black",font = ctk.CTkFont(family = "Helvetica",weight = "normal",size = 15), command = self.navigate_to_home)
        self.back_button.pack(side = "top",anchor = "w", pady = 10, padx = 10)


        self.leader_lbl = ctk.CTkLabel(self.main_frame,text = "LEADER BOARD",text_color="#000000",fg_color="#ffffff",font = ctk.CTkFont(family = "Impact",size = 45,weight = "normal"))
        self.leader_lbl.pack(side = "top",padx = 200)

        self.text_frame = ctk.CTkFrame(self.main_frame,fg_color="#ffffff")
        self.text_frame.pack(fill = "x",padx = (25,25),pady = (10,0))

        self.date_lbl = ctk.CTkLabel(self.text_frame,text="Date",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.date_lbl.place(x = 50,y = 50)

        self.rank_lbl = ctk.CTkLabel(self.text_frame,text="Rank",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.rank_lbl.place(x = 270,y = 50)

        self.name_lbl = ctk.CTkLabel(self.text_frame,text="Name",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.name_lbl.place(x = 500,y = 50)

        self.score_lbl = ctk.CTkLabel(self.text_frame,text="Score",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.score_lbl.place(x = 770,y = 50)

        self.time_lbl = ctk.CTkLabel(self.text_frame,text="Time",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.time_lbl.place(x = 1050,y = 50)

    def navigate_to_home(self):
        self.navigate_frame_method("leaderboard","homepage")



# leader = LeaderBoard()
# leader.mainloop()
