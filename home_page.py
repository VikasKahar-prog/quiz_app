import customtkinter as ctk 
import tkinter as tk
from PIL import Image,ImageTk
from name_page import NamePage
from leader import LeaderBoard

class HomePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()        
        self.geometry('{}x{}+{}+{}'.format(self.width,self.height,-10,0))
        #self.config(bg="#ffbe0b")
        self.title("QUIZ APP")
        print(self.width, self.height)

        self.frames = {}

        self.container_frame = ctk.CTkFrame(self)
        self.container_frame.pack(fill = "both",expand = True)

        self.home_frame = ctk.CTkFrame(self.container_frame,fg_color="#ffbe0b")
        self.home_frame.pack(fill = "both",expand = True)

        # self.home_frame.pack(fill = "both",expand = True)

        self.add_frames("homepage",self.home_frame)
        
        self.bgimage = ctk.CTkImage(dark_image=Image.open("images/img1.jpg"),size=(400, 400))
        self.bglabel = ctk.CTkLabel(self.home_frame,image = self.bgimage,text = "",bg_color="transparent")
        self.bglabel.pack(anchor='w',padx=100,pady=80)

        self.logo_frame = ctk.CTkFrame(self.home_frame, fg_color="#001d3d")
        self.logo_image = ctk.CTkImage(dark_image=Image.open("images/Screenshot_2025-01-11_153522-removebg-preview.png"),size=(400, 100))
        self.logo_label = ctk.CTkLabel(self.logo_frame,image = self.logo_image,text = "")
        self.logo_label.pack()

        self.logo_frame.pack(anchor='w',padx=100)

        self.text_frame = ctk.CTkFrame(self.home_frame, fg_color="#ffbe0b", bg_color="#ffbe0b")
        self.text1 = ctk.CTkLabel(self.text_frame, text="Let's play", text_color="#001d3d", font=ctk.CTkFont(family="jokerman",weight="bold", size=40))
        self.text1.pack(side = tk.LEFT)
        self.text2 = ctk.CTkLabel(self.text_frame, text="Quiz", text_color="#001d3d", font=ctk.CTkFont(family="jokerman",weight="bold", size=90))
        self.text2.pack(padx = 10, side = tk.RIGHT)
        self.text_frame.place(x = 800, y = 250)

        self.start_button = ctk.CTkButton(self.home_frame, text="START", fg_color="#001d3d", text_color="white", height=45, width=200, font=ctk.CTkFont(family="Verdana Pro", size=20, weight="bold"), corner_radius=10, bg_color="#ffbe0b",command=self.navigate_screen_to_namepage)
        self.start_button.place(x = 900, y = 430)

        self.leader_board_image = ctk.CTkImage(dark_image=Image.open("images//winner.png"), light_image=Image.open("images//winner.png"), size=(100, 100))
        self.ld_board_button = ctk.CTkButton(self.home_frame, text = "", hover=False, image = self.leader_board_image, fg_color="#ffbe0b", bg_color="#ffbe0b",cursor = "hand2",command=self.navigate_screen_to_leaderboard)
        self.ld_board_button.place(x = 1220, y = 20)

        # self.ld_board_button = ctk.CTkButton(self.home_frame, text="", image=self.leader_board_image, fg_color="#ffbe0b", bg_color="#003049", hover=False, cursor = "hand2",command=self.navigate_screen_to_leaderboard)
        # self.ld_board_button.pack(side = "top")

    def add_frames(self,name,frame_object):
        self.frames[name] = frame_object

    def navigate_between_frames(self,old_frame,new_frame):
        if old_frame:
            self.frames[old_frame].pack_forget()
            
        render_frame =  self.frames[new_frame]
        render_frame.pack(fill = "both",expand = True)

    def navigate_screen_to_namepage(self):
        name_page_object = NamePage(self.container_frame,self.add_frames,self.navigate_between_frames,"NamePage")
        self.navigate_between_frames("homepage","namepage")

    def navigate_screen_to_leaderboard(self):
        leader_board_object = LeaderBoard(self.container_frame,self.add_frames,self.navigate_between_frames,"Leader Board")
        self.navigate_between_frames("homepage","leaderboard")
    
if __name__ == "__main__":
    quiz_app = HomePage()
    quiz_app.mainloop()
