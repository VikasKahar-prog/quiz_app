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

        self.leader_lbl = ctk.CTkLabel(self.main_frame,text = "LEADER BOARD",text_color="#000000",fg_color="#ffffff",font = ctk.CTkFont(family = "Impact",size = 45,weight = "normal"))
        self.leader_lbl.pack(side = "top",padx = 200)

        self.text_frame = ctk.CTkFrame(self.main_frame,fg_color="#ffffff")
        self.text_frame.pack(fill = "x",padx = (25,25),pady = (10,0))

        self.date_lbl = ctk.CTkLabel(self.text_frame,text="Date",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.date_lbl.place(x = 30,y = 50)

        self.rank_lbl = ctk.CTkLabel(self.text_frame,text="Rank",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.rank_lbl.place(x = 250,y = 50)

        self.name_lbl = ctk.CTkLabel(self.text_frame,text="Name",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.name_lbl.place(x = 480,y = 50)

        self.score_lbl = ctk.CTkLabel(self.text_frame,text="Score",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.score_lbl.place(x = 750,y = 50)

        self.time_lbl = ctk.CTkLabel(self.text_frame,text="Time",text_color="#000000",font=ctk.CTkFont(family = "Helvetica",size = 35,weight = "normal"))
        self.time_lbl.place(x = 1030,y = 50)



# leader = LeaderBoard()
# leader.mainloop()
